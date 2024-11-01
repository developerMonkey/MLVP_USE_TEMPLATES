from mlvp import *
import random
#from 验证模块的dut类库 import *
#from UT_dual_port_stack import *
#Bundle 来描述需要驱动的某类接口
class xxxxxxBundle(Bundle):
    #变量名与目标verilog模块接口命名映射,    根据verilog模块定义端口变量定义
    clk,rst,in_valid,in_ready,in_data,in_cmd,out_valid,out_ready,out_data,out_cmd = Signals(10)
from mlvp.agent import *
#Agent 用于编写对该接口的驱动方法
#Bundle 是该 Agent 需要驱动的接口的描述。
# 在 Bundle 中提供了一系列的连接方法来连接到 DUT 的输入输出端口。
# 这样一来，我们可以通过此 Agent 完成所有拥有相同接口的 DUT 的驱动操作

class xxxxxxAgent(Agent):

    def __init__(self, bundle:xxxxxxBundle):
        super().__init__(xxxxxxBundle.step)
        self.bundle = xxxxxxBundle #xxxxxxBundle更换为以上定义的bundle

    #此处编写验证逻辑 example:
    @driver_method()
    def callback(cycles):
        print(f"The current clock cycle is {cycles}")
        
    @driver_method()
    async  def push(self):
        self.port_dict["in_valid"]= 1
        self.port_dict["in_cmd"] = random.randint(0, 1)
        self.port_dict["in_data"] = random.randint(0, 2**32-1)
    @driver_method()
    async def pop(self):
        self.port_dict["in_valid"] = 1
        self.port_dict["in_cmd"] = random.randint(0, 1)    

from mlvp.model import * 
#使用 Model 来定义参考模型用于验证verilog功能的输出是否正确
class xxxxxxModel(Model):
    def __init__(self):
        super().__init__()

        self.push_port = DriverPort(agent_name="port_agent", driver_name="push")
        self.pop_port = DriverPort(agent_name="port_agent", driver_name="pop")  

from mlvp.env import *
#创建一个顶层的测试环境Env，将上述的驱动方法与参考模型相关联

class xxxxxxEnv(Env):
    #将测试环境与被测试dut绑定,初始化其他参数按需求定义,初始化参数可以有多个，但是必须有dut
    def __init__(self,dut):
        super().__init__()
        xxxxxx_bundle = xxxxxxBundle.from_prefix("in0_").bind(dut)  #将验证bundle与被验证verilog模块的dut端口连接绑定
        
        self.xxxxxx_agent = xxxxxxAgent(xxxxxx_bundle) ##bundle与agent绑定
                    