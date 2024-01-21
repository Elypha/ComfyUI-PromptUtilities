

class PromptUtilitiesFormatString:
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "prompt": ("STRING", {"default": "[1], [2]", "display": "prompt"}),
            },
            "optional": {
                "arg1": ("STRING",{"forceInput": True}),
            },
        }
        # for i in range(1, MAX_NUM_ARGS + 1):
        #     arg_name = f"arg{i}"
        #     input_types["optional"][arg_name] = ("STRING", {"default": "", "display": arg_name})

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "format"

    CATEGORY = "PromptUtilities"

    def format(self, prompt, **kwargs):
        print(kwargs)
        result = prompt
        for i in range(1, len(kwargs) + 1):
            result = result.replace(f'[{i}]',kwargs[f"arg{i}"]) 
        return (result,)
    

class PromptUtilitiesJoinStringList:
    @classmethod
    def INPUT_TYPES(s):
        input_types = {
            "required": {
                "separator": ("STRING", {"default": ", ", "display": "separator"}),
            },
            "optional": {
                "arg1": ("STRING",{"forceInput": True}),
            },
        }

        return input_types

    RETURN_TYPES = ("STRING",)
    FUNCTION = "join"

    CATEGORY = "PromptUtilities"

    def join(self, separator, **kwargs):
        print(kwargs)
        print(kwargs.values())
        result = separator.join(kwargs.values())
        return (result,)