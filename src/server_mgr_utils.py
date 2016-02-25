#!/usr/bin/python

import re
# vim: tabstop=4 shiftwidth=4 softtabstop=4
"""
   Name : server_mgr_utils.py
   Author : Abhay Joshi
   Description : generic utility functions for server manager code.
"""
__version__ = '1.0'

class ServerMgrUtil():
    def convert_unicode():
        def convert_unicode(input):
            if isinstance(input, dict):
                return {convert_unicode(key): convert_unicode(value) for key, value in input.iteritems()}
            elif isinstance(input, list):
                return [convert_unicode(element) for element in input]
            elif isinstance(input, unicode):
                return input.encode('utf-8')
            else:
                return input
        # end convert_unicode(input)
        return convert_unicode
    convert_unicode = staticmethod(convert_unicode())
  
    def get_package_version(self,package_name):
        exp = re.compile("[0-9].*")
        for m in exp.finditer(package_name):
            match_index = m.span()[0]
            version = package_name[match_index:-4]
        return version

if __name__ == '__main__':
    # test code
    print ServerMgrUtil.convert_unicode(u'this is converted unicode string')
    sm = ServerMgrUtil()
    print sm.get_package_version('/root/contrail-install-packages-3.0-2712~juno.el7.centos.noarch.rpm')
