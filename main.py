import os
import json
import pygame
from load_image import load_image, load_cars_image
from road import Road, RoadsList
from car import Car, CarsList
from spawner import VehicleSpawner, VehicleSpawnersList


pygame.init()
os.system('cls' if os.name == 'nt' else 'clear  ')
pygame.display.set_caption('Just text stub')
screen = pygame.display.set_mode((650, 650))
clock = pygame.time.Clock()

car_sprites = pygame.sprite.Group()
cars = CarsList()

image_folder = os.path.join(os.getcwd(), 'images')

bg_image_path = os.path.join(image_folder, 'bg-road-2.png')
background = pygame.transform.scale(load_image(bg_image_path), (650, 650))

cars_path = os.path.join(image_folder, 'cars.png')
cars_images = load_cars_image(cars_path, (25, 50))

roads = RoadsList()
with open('co-road.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)
for i in data.values():
    road_id = i.get('road-id')
    road_points = i.get('road-points')
    next_roads = i.get('next-roads')
    obj = Road(road_id, road_points, next_roads)
    all_roads = roads.roads
    all_roads[road_id] = obj
    roads.roads = all_roads

# spawners
vspawners = VehicleSpawnersList(3)
possible_roads = ["#1", "#7", "#13", "#19"]
for i in range(4):
    spawner_road = roads.roads.get(possible_roads[i])
    sizes = {
        'car': (20, 40)
    }
    spawner = VehicleSpawner(spawner_road, ['car'], sizes)
    a = vspawners.spawners
    a.append(spawner)
    vspawners.spawners = a

run = True
while run:
    events = pygame.event.get()
    for event in events:
        etype = event.type
        if etype == pygame.QUIT:
            run = False
            break
    # background
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # mouse pos
    pos = pygame.mouse.get_pos()
    font = pygame.font.Font(None, 24)
    text = font.render(f'Mouse: {pos}', 1, (255, 0, 0))
    screen.blit(text, (0, 0))
    # road lines
    for road in roads.roads.values():
        road_id = road.road_id  # road id
        font = pygame.font.Font(None, 20)
        points = road.road_points
        pos = points[0]
        text = font.render(road_id, 1, (255, 0, 0))
        screen.blit(text, pos)
        for i in range(len(points) - 1):  # road points
            pygame.draw.line(screen, (0, 0, 255), points[i], points[i + 1], 3)
        next = road.next_roads  # next roads
        if next is None:
            continue
        for i in next:
            point = roads.roads.get(i).road_points[0]
            pygame.draw.line(screen, (0, 255, 0), points[-1], point, 3)
    car_sprites.draw(screen)
    car_sprites.update(screen, roads)
    for car in cars.cars:
        pygame.draw.rect(screen, (255, 0, 0), car.rect, 2)
    vspawners.update(car_sprites)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
