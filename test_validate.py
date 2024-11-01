import pytest
from mlvp import *
from verification_Env import *
import os,sys
#from 验证模块的dut类库 import *
#from UT_dual_port_stack import *


#mlvp 提供了 mlvp_async 标记来标记异步测试用例
#只需要在测试用例函数上添加 @pytest.mark.mlvp_async 标记，pytest 就能够直接运行协程测试用例
@pytest.mark.mlvp_async
#xxxxx_dut 是dut对象
async def test_send_req(xxxxx_dut):
    start_clock(xxxxx_dut) #绑定时钟

    #此处调用agent定义的验证逻辑
    #参数使用Env定义的初始化参数对象,定义的Env类，根据初始化方法赋值
    env = xxxxxxEnv(xxxxx_dut)

    
    
    

#Fixture 是 pytest 中的概念  
# pytest 将会自动调用 adder_dut Fixture，并将其返回值传入测试用例  
#创建测试DUT对象
@pytest.fixture()
def dual_port_stack_dut(mlvp_pre_request:PreRequest):
    setup_logging(INFO)
    #根据DUT对象生成Env对象 ,
    # DUTxxxxxx为由picker验证模块的dut类对象
    return mlvp_pre_request.create_dut(DUTxxxxxx) 