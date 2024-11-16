import matplotlib.pyplot as plt

file_path = 'DS2.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()

coordinates = [tuple(map(int, line.strip().split())) for line in data]
canvas_size = (960, 540)
plt.figure(figsize=(canvas_size[0] / 100, canvas_size[1] / 100))

x, y = zip(*coordinates)
plt.scatter(x, y, s=1, color='blue')

plt.axis('off')
plt.gca().set_aspect('equal', adjustable='box')

output_file = 'результат.png'
plt.savefig(output_file, dpi=100, bbox_inches='tight', pad_inches=0)
plt.show()
print(f"Зображення збережено у файл {output_file}")