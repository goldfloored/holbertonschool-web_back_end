#!/usr/bin/env python3
"""
API Authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Authentication Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Authentication
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """
        Authorization
        """
        if request is None:
            return None
        if not request.headers.get("Authorization"):
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current user
        """
        return None