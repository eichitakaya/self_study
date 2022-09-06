is_simple_core = False

if is_simple_core:
    from sophon.core_simple import Variable
    from sophon.core_simple import Function
    from sophon.core_simple import using_config
    from sophon.core_simple import no_grad
    from sophon.core_simple import as_array
    from sophon.core_simple import as_variable
    from sophon.core_simple import setup_variable

else:
    from sophon.core import Variable
    from sophon.core import Function
    from sophon.core import Parameter
    from sophon.core import using_config
    from sophon.core import no_grad
    from sophon.core import as_array
    from sophon.core import as_variable
    from sophon.core import setup_variable
    
    from sophon.layers import Layer
    from sophon.models import Model
    
    from sophon.datasets import Dataset
    from sophon.dataloaders import DataLoader
    
    import sophon.functions
    import sophon.layers
    import sophon.transforms

setup_variable()