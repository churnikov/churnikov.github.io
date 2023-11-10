import js
from pyodide.ffi import create_proxy



async def onclick(e):
    ketcher = js.document.getElementById("ifKetcher").contentWindow.ketcher
    smiles = await ketcher.getSmiles()
    mol_placeholder = js.document.getElementById("mol-placeholder")
    mol_placeholder.innerHTML = smiles
    print(smiles)


def main():
    button = js.document.getElementById("get-mol-btn")
    button.addEventListener("click", create_proxy(onclick))


main()
