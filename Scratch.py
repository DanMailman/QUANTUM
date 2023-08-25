# Scratch.py - Scratch Wokspace for Temporary Development
from qiskit import __qiskit_version__
def PrintQiskitVersions():
    # init_qiskit(): Indicate qiskit is available
    # Implementation: print() on qiskit.__qiskit_version__
    for k,v in __qiskit_version__:

    print(f'__qiskit_version__: {__qiskit_version__}')
    __qiskit_version__


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_qiskit()
    __qiskit_version__

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
