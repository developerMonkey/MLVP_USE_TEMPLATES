# MLVP_USE_TEMPLATES
Digital Circuit Verification libaray used templates
一、Picker工具

依赖安装

cmake ( >=3.11 )
gcc ( 支持c++20,至少为gcc版本10, 建议11及以上 )
python3 ( >=3.8 )
verilator ( ==4.218 )
verible-verilog-format ( >=0.0-3428-gcfcbb82b )
swig ( >=4.2.0, 用于多语言支持 )
下载链接https://github.com/XS-MLVP/picker.git

二、pytest工具 建议使用7.0.0版本以上

pip install -U pytest
# 查看pytest版本
pytest --version
# 查看已安装包列表
pip list
# 查看pytest帮助文档
pytest -h
# 安装第三方插件
pip install pytest-sugar
pip install pytest-rerunfailures
pip install pytest-xdist
pip install pytest-assume
pip install pytest-html

模版文件放在picker生成的dut文件夹下与UT_xxx同目录

三、MLVP工具（建议使用最新版本）

支持生成功能覆盖率

下载链接https://github.com/XS-MLVP/mlvp
