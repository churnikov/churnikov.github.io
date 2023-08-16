import js


def set_mol(ketcher_window_id, smiles):
    ketcher = js.document.getElementById(ketcher_window_id).contentWindow.ketcher
    ketcher.setMolecule(smiles)

