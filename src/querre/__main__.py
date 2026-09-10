#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Querre: __main__.py
#
# Copyright © 2026 Shinichiro Ikeda
#
# This software is released under the MIT license.
# see https://opensource.org/licenses/MIT


import sys


#================================================================================
if __name__ == '__main__':

	# パラメータ取得
	args = sys.argv[1:]

	# パラメータ取得(-V, --version)
	if '-V' in args or '--version' in args:
		# パッケージのバージョンを動的に取得して表示する
		import importlib.metadata
		package_name = "querre"
		try:
			version = importlib.metadata.version(package_name)
			print(f"{package_name} {version}")
		except importlib.metadata.PackageNotFoundError:
			print(f"{package_name} is not installed")
		sys.exit()

	# パラメータ取得(--help)
	if '--help' in args:
		print(f"usage: {__package__} [--help] [-V|--version]")
		sys.exit()

# EOF
