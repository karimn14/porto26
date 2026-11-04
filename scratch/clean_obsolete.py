import os

obsolete = [
    'batik-coagulant-unit.html',
    'funbox-controller.html',
    'humanoid-robot-dance.html',
    'intelligent-ev-charging-station.html',
    'wind-turbine-3d-model.html'
]

for sub in ['', 'project']:
    for name in obsolete:
        p = os.path.join(r'd:\project\porto26', sub, 'projects', name)
        if os.path.exists(p):
            os.remove(p)
            print(f'Removed {p}')

print('Obsolete files cleaned up.')

