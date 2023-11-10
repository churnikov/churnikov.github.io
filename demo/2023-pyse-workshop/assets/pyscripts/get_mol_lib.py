import js


def get_molecule_from_input(input_id):
    input = js.document.getElementById(input_id)
    return input.value


async def get_molecule_from_ketcher(ketcher_window_id):
    ketcher = js.document.getElementById(ketcher_window_id).contentWindow.ketcher
    return await ketcher.getSmiles()


async def set_molecule_in_div():
    mol = await get_molecule_from_ketcher('ketcher-demo')
    js.document.getElementById('5-molecule-div').innerHTML = mol
