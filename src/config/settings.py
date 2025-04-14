import yaml
import os

# 加载配置文件
def load_config():
    """
    从当前目录加载 config.yml 配置文件
    """
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.yml")

    # 检查配置文件是否存在
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"配置文件未找到：{config_path}")

    print(f"正在加载配置文件：{config_path}")

    # 加载配置文件内容
    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    print("配置文件加载成功，内容如下：")
    for key, value in config.items():
        print(f"  {key}: {value}")

    return config

print(f"正在加载配置...")
# 加载配置
config = load_config()

# 从配置文件中读取配置
model = config.get("model", "default-model")
max_tokens = config.get("max_tokens", 100)
temperature = config.get("temperature", 0.7)
api_url = config.get("api_url", "https://default-api-url.com")
api_key = config.get("api_key") or os.getenv("SILICON_API_KEY")  # 优先从配置文件读取，否则从环境变量加载
output_dir = config.get("output_dir", os.path.join(os.getcwd(), "output"))  # 默认输出目录为当前目录下的 "output"

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"输出目录不存在，已创建：{output_dir}")
else:
    print(f"输出目录已存在：{output_dir}")
