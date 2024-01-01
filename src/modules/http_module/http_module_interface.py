# -*- coding: utf-8 -*-
# Author:       Paulo Jacob
# Description:  Interface by make requests
# Created at:   12-28-2023
from abc import ABC, abstractmethod


class HTTPModuleInterface(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def patch(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def put(self):
        pass
