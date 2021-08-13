import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
from pythonjsonlogger import jsonlogger

# def setup_logging_1(func, **kwargs):
    
#     def wrapper(*args, **kwargs):
    
#         try:
#             log_dict =kwargs['log_dict']
#             log_level=logging.INFO
#             logger = logging.getLogger() 
#             assert len(logger.handlers) == 1
#             logger.setLevel(log_level)
#             json_handler = logging.StreamHandler()
#             formatter = jsonlogger.JsonFormatter(
                
#                 fmt='%(asctime)s %(levelname)s %(pathname)s, %(lineno)d %(source)s %(api_id)s %(pinpoint_id)s %(mobile)s  %(message)s',
#                 datefmt='%d/%m/%Y %H:%M:%S')
#             json_handler.setFormatter(formatter)
#             logger.addHandler(json_handler)
#             logger.removeHandler(logger.handlers[0])
#             kwargs ={"log_dict":log_dict, "logger":logger}
                        
#             return func(*args, **kwargs)
#         except Exception as e:
#             logger.exception(str(e))
#     return wrapper
    
    
    
    
    
class setup_logging(object):
    
    formatter = '%(asctime)s %(levelname)s %(pathname)s %(lineno)d %(message)s'
    
    def __init__(self, *args):
        self.log_dict = {key:None for key in args} 
        self.formatter = setup_logging.formatter
        for key in args:
            self.formatter += f" %({key})s"

    def __call__(self, func, *args, **kwargs):
    
        def wrapper(*args, **kwargs):
            try:
                log_level=logging.INFO
                logger = logging.getLogger() 
                assert len(logger.handlers) == 1
                logger.setLevel(log_level)
                json_handler = logging.StreamHandler()
                formatter = jsonlogger.JsonFormatter(
                    fmt=self.formatter,
                    datefmt='%d/%m/%Y %H:%M:%S')
                    
                json_handler.setFormatter(formatter)
                logger.addHandler(json_handler)
                logger.removeHandler(logger.handlers[0])
                kwargs ={"log_dict":self.log_dict, "logger":logger}
                return func(*args, **kwargs)
            except Exception as e:
                print(str(e))
                logger.exception(str(e))
                #pass
        return wrapper
