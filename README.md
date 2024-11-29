# streamlit_pose_yolov8

```
ImportError: This app has encountered an error. The original error message is redacted to prevent data leaks. Full error details have been recorded in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling
    result = func()
             ^^^^^^
File "/home/adminuser/venv/lib/python3.12/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec
    exec(code, module.__dict__)
File "/mount/src/streamlit_pose_yolov8/app.py", line 4, in <module>
    from ultralytics import YOLO
File "/home/adminuser/venv/lib/python3.12/site-packages/ultralytics/__init__.py", line 11, in <module>
    from ultralytics.models import NAS, RTDETR, SAM, YOLO, FastSAM, YOLOWorld
File "/home/adminuser/venv/lib/python3.12/site-packages/ultralytics/models/__init__.py", line 3, in <module>
    from .fastsam import FastSAM
File "/home/adminuser/venv/lib/python3.12/site-packages/ultralytics/models/fastsam/__init__.py", line 3, in <module>
    from .model import FastSAM
File "/home/adminuser/venv/lib/python3.12/site-packages/ultralytics/models/fastsam/model.py", line 5, in <module>
    from ultralytics.engine.model import Model
File "/home/adminuser/venv/lib/python3.12/site-packages/ultralytics/engine/model.py", line 11, in <module>
    from ultralytics.cfg import TASK2DATA, get_cfg, get_save_dir
File "/home/adminuser/venv/lib/python3.12/site-packages/ultralytics/cfg/__init__.py", line 10, in <module>
    import cv2
File "/home/adminuser/venv/lib/python3.12/site-packages/cv2/__init__.py", line 181, in <module>
    bootstrap()
File "/home/adminuser/venv/lib/python3.12/site-packages/cv2/__init__.py", line 153, in bootstrap
    native_module = importlib.import_module("cv2")
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/usr/local/lib/python3.12/importlib/__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)

```
