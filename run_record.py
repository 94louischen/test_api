# -*- coding: utf-8 -*-
# @Time : 2021/9/9 14:20
# @Author : chenxuan
"""
运行录制脚本的命令
"""
import os

os.system("mitmweb -p 7777 -s tools/recording.py")
