=====配置运行环境=====
1.安装python-2.7.14.amd64.msi，（不要修改安装路径，或对应修改后续所有路径）
2.将numpy-1.13.3+mkl-cp27-cp27m-win_amd64.whl和
    opencv_python-2.4.13.2-cp27-cp27m-win_amd64.whl
    拷贝至C:\Python27\Script\
3.键盘windows+R,在运行对话框内键入cmd，回车
4.输入 cd C:\Python27\Scripts\  回车
5.输入 pip.exe install numpy-1.13.3+mkl-cp27-cp27m-win_amd64.whl 回车
6.输入 pip.exe install opencv_python-2.4.13.2-cp27-cp27m-win_amd64.whl 回车
7.修改环境变量：在 此电脑->属性->高级系统设置->高级->环境变量->系统变量 
                为 Path 变量增加 C:\Python27\
至此，运行环境配置结束
=====运行执行脚本=====
（将cvtImage.py脚本与所有需要转换的视频放置在同一文件夹内，以E:\video为例）
1.键盘windows+R,在运行对话框内键入cmd，回车
2.输入 E: (对应的磁盘）
3.输入 cd E:\video (对应的路径）
4.输入 python cvtImage.py 回车，运行，等待结果
至此，执行结束，结果在image文件夹内