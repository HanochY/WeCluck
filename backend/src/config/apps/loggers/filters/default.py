import logging
import re

SENSITIVE_KEYS = (
        "credentials",
        "authorization",
        "token",
        "password",
        "access_token",
    )
GENERIC_TOKEN_PATTERN = rf"token=([^;]+)"
BEARER_TOKEN_PATTERN = rf"Bearer\s+([a-zA-Z0-9\-._~+/]+=*)"
    
class SensitiveDataFilter(logging.Filter):
    def filter(self, record):
        try:
            record.args = self.mask_sensitive_args(record.args)
            record.msg = self.mask_sensitive_msg(record.msg)
            return True
        except Exception as e:
            return True

    def mask_sensitive_args(self, args):
        if isinstance(args, dict):
            new_args = args.copy()
            for key in args.keys():
                if key.lower() in self.SENSITIVE_KEYS:
                    new_args[key] = "******"
                else:
                    new_args[key] = self.mask_sensitive_msg(args[key])
            return new_args
        return tuple([self.mask_sensitive_msg(arg) for arg in args])

    def mask_sensitive_msg(self, message):
        if isinstance(message, dict):
            return self.mask_sensitive_args(message)
        if isinstance(message, str):
            message = re.sub(self.GENERIC_TOKEN_PATTERN, f"token=******", message)
            message = re.sub(self.BEARER_TOKEN_PATTERN, f"bearer ******", message)
        return message
