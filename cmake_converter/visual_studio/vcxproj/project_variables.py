#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016-2018:
#   Matthieu Estrada, ttamalfor@gmail.com
#   Pavel Liavonau, liavonlida@gmail.com
#
# This file is part of (CMakeConverter).
#
# (CMakeConverter) is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# (CMakeConverter) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with (CMakeConverter).  If not, see <http://www.gnu.org/licenses/>.

from cmake_converter.project_variables import ProjectVariables


class VCXProjectVariables(ProjectVariables):
    """
        Class who defines all the CMake variables to be used by the C/C++ project
    """

    @staticmethod
    def set_root_namespace(context, node):
        context.root_namespace = node.text

    @staticmethod
    def set_windows_target_version(context, node):
        context.target_windows_version = node.text

    def set_output_dir(self, context, node):
        self.set_output_dir_impl(context, node.text)

    def set_output_file(self, context, output_file_node):
        if output_file_node is not None:
            self.set_output_file_impl(context, output_file_node.text)

    def set_import_library(self, context, node):
        self.set_path_and_name_from_node(
            context,
            'Import library',
            node.text,
            'ARCHIVE_OUTPUT_DIRECTORY',
            'ARCHIVE_OUTPUT_NAME'
        )

    def set_program_database_file(self, context, node):
        self.set_path_and_name_from_node(
            context,
            'Program database',
            node.text,
            'PDB_OUTPUT_DIRECTORY',
            'PDB_NAME'
        )
