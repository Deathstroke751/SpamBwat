from dotenv import dotenv_values
import ast

config_file = 'config.env'


def env_bool(variable, config_file=config_file) -> bool:
    config_env = dotenv_values(config_file)
    return ast.literal_eval(config_env[variable])


def env_dict(variable, config_file=config_file) -> dict:
    config_env = dotenv_values(config_file)
    return ast.literal_eval(config_env[variable])


def env_list(variable, config_file=config_file) -> list:
    config_env = dotenv_values(config_file)
    return ast.literal_eval(config_env[variable])


def env_str(variable, config_file=config_file) -> str:
    config_env = dotenv_values(config_file)
    return config_env[variable]


if __name__ == '__main__':
    print(type(env_bool('AUCTION_STATUS')), env_bool('AUCTION_STATUS'))
    print(type(env_dict('PUBLICNODE_HTTPS')), env_dict('PUBLICNODE_HTTPS'))
    print(type(env_list('INFURA_API')), env_list('INFURA_API'))
    print(env_dict('EXPLORER')[env_str('NETWORK')])
