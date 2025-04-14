from enum import Enum
from inspect import getmembers, isroutine
from datetime import date, datetime
import traceback
from types import NoneType
import uuid
from dataclasses import asdict


from asyncpg.pgproto import pgproto
from pydantic import BaseModel
from sqlalchemy import String
from .casedict import CaseDict
from .object_mapper_exception import ObjectMapperException


class ObjectMapper:
    """
    Base class for mapping class attributes from one class to another.
    Supports mapping conversions too.
    """

    primitive_types = {
        int,
        float,
        str,
        bool,
        date,
        datetime,
        pgproto.UUID,
        uuid.UUID,
        NoneType,
    }
    mappings = {}  # Class-level dictionary for mappings

    @classmethod
    def create_map(cls, type_from, type_to, mapping=None):
        """Creates a mapping between two types."""
        # Allow BaseModel-derived classes or standard types
        if not isinstance(type_from, type) or not (
            issubclass(type_from, BaseModel) or issubclass(type_from, object)
        ):
            raise ObjectMapperException(
                "type_from must be a class or BaseModel-derived type."
            )

        if not isinstance(type_to, type) or not (
            issubclass(type_to, BaseModel) or issubclass(type_to, object)
        ):
            raise ObjectMapperException(
                "type_to must be a class or BaseModel-derived type."
            )

        if mapping is not None and not isinstance(mapping, dict):
            raise ObjectMapperException("Mapping must be a dictionary.")

        if type_from not in cls.mappings:
            cls.mappings[type_from] = {}
        if type_to in cls.mappings[type_from]:
            raise ObjectMapperException(
                f"Mapping for {type_from} -> {type_to} already exists."
            )

        cls.mappings[type_from][type_to] = (type_to, mapping)

    @classmethod
    def map(
        cls,
        from_obj,
        to_type=type(None),
        ignore_case=False,
        allow_none=False,
        excluded=None,
        included=None,
        allow_unmapped=False,
    ):
        """Maps an object of one type to another."""
        if from_obj is None and allow_none:
            return None
        if from_obj.__class__ in cls.primitive_types:
            return from_obj

        if not from_obj:
            raise ObjectMapperException("Source object cannot be None.")

        key_from = from_obj.__class__

        if key_from not in cls.mappings:
            raise ObjectMapperException(f"No mapping defined for {key_from}.")

        if to_type is None or to_type is type(None):
            if len(cls.mappings[key_from]) > 1:
                raise ObjectMapperException(
                    f"Ambiguous mapping for {key_from}, specify to_type explicitly."
                )
            key_to = next(iter(cls.mappings[key_from]))
        else:
            if to_type not in cls.mappings[key_from]:
                raise ObjectMapperException(
                    f"No mapping defined for {key_from} -> {to_type}."
                )
            key_to = to_type

        custom_mappings = cls.mappings[key_from][key_to][1]
        if hasattr(key_to, "empty"):
            inst = key_to.empty()
        elif issubclass(key_to, BaseModel):
            inst = key_to.model_construct()
        else:
            inst = key_to()

        # from_props = getmembers(from_obj, lambda a: not isroutine(a))
        # to_props = getmembers(inst, lambda a: not isroutine(a))

        # from_dict = {k: v for k, v in from_props if not k.startswith("_")}
        # to_dict = {k: v for k, v in to_props if not k.startswith("_")}

        def not_private(s):
            return not s.startswith("_")

        def not_excluded(s):
            return not (excluded and s in excluded)

        from_obj_dict = {
            k: v
            for k, v in from_obj.__dict__.items()
            if not_private(k) and not_excluded(k)
        }

        if issubclass(key_to, BaseModel):
            to_obj_dict = {
                k: v for k, v in inst.model_fields.items() if not_private(k)
            }
        else:
            to_obj_dict = {
                k: v for k, v in asdict(inst).items() if not_private(k)
            }
        if ignore_case:
            from_dict = CaseDict(from_obj_dict)
            to_dict = CaseDict(to_obj_dict)
        else:
            from_dict = from_obj_dict
            to_dict = to_obj_dict

        # if ignore_case:
        #     from_dict = CaseDict(from_dict)
        #     to_dict = CaseDict(to_dict)

        def map_value(value):
            if isinstance(value, list):
                return [
                    cls.map(
                        v,
                        type(None),
                        ignore_case,
                        allow_none,
                        excluded,
                        included,
                        allow_unmapped,
                    )
                    for v in value
                ]
            if value.__class__ in cls.mappings:
                return cls.map(
                    value,
                    type(None),
                    ignore_case,
                    allow_none,
                    excluded,
                    included,
                    allow_unmapped,
                )
            if value.__class__ in cls.primitive_types:
                return value
            if issubclass(value.__class__, Enum):
                return value
            if allow_unmapped:
                return value
            raise ObjectMapperException(
                f"No mapping defined for {value.__class__}."
            )

        for prop in to_dict.keys():
            if prop in from_dict:
                value = map_value(from_dict[prop])
                setattr(inst, prop, value)
            elif custom_mappings and prop in custom_mappings:
                mapping_fn = custom_mappings[prop]
                setattr(
                    inst, prop, mapping_fn(from_obj) if mapping_fn else None
                )

        return inst
