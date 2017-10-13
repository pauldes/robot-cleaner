@echo off
IF "%~1"=="install" pip install pygal
IF "%~1"=="run" python Graph.py & echo Results are available in graph_rendering.svg & start graph_rendering.svg
