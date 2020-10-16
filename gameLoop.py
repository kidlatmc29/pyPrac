#Skeleton game loop
import pygame

def main():
  pygame.init()
  pygame.display.set_caption("we tryin")
  window_size = 500

  window = pygame.display.set_mode((window_size, window_size))

  rec = (300, 200, 150, 90)
  color = (255, 0, 0)

  while True :
    event = pygame.event.poll()
    if event.type == pygame.QUIT :
      print("game is quitting")
      break
    #this is where you'd update game data
    window.fill((0,255,0))

    window.fill(color, rec)
    pygame.display.flip()

  pygame.quit()

main()