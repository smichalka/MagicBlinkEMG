from pylsl import StreamInfo, StreamOutlet
import pygame

def display_sentence(texts, screen, font):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GRAY = (200, 200, 200)
    WHITE = (255,255,255)
    BLUE = (50,50,200)
    screen.fill(WHITE)
    y_offset = 0
    for text in texts:
        fw, fh = font.size(text)
        img = font.render(text, True, BLUE)
        screen.blit(img, (200, 200+y_offset))
        y_offset += fh
    pygame.display.update()

def wait_for_keypress():
    running = True
    while running:
        # creating a loop to check events that
        # are occuring
        for event in pygame.event.get():
            # checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:
                # creating display            
                running = False
                print("running false")
                break

def generate_next_stimulus_msg(stimulus):
    return [f" < {stimulus} > "]

def main():
    hand_motions = ['snap', 'squeeze', 'tap', 'nothing']

    marker_stream_name = "MyMarkerStream"
    info = StreamInfo(marker_stream_name, 'Markers', 1, 0, 'string')
    outlet = StreamOutlet(info)

    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    font = pygame.font.SysFont(None, 54)
    display_sentence(["Press any key to being"], screen, font)
    wait_for_keypress()

    display_sentence(["Type 'q' to quit,", "'n' or ' ' for next,", "'c' when completed speaking"],screen,font)
    pygame.display.update()
    pygame.time.delay(1000)

    begin_trial = True
    current_stimulus = 0
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and begin_trial:
                    stimulus = generate_next_stimulus_msg(f'{hand_motions[current_stimulus]} start')
                    display_sentence(stimulus, screen, font)
                    outlet.push_sample([f"{current_stimulus}"])
                    begin_trial = False
                elif event.key == pygame.K_SPACE:
                    stimulus = generate_next_stimulus_msg(f'{hand_motions[current_stimulus]} finish')
                    display_sentence(stimulus, screen, font)
                    outlet.push_sample([f"{current_stimulus}"])
                    begin_trial = True
                    current_stimulus += 1
                    if current_stimulus >= 4:
                        current_stimulus = 0
                elif event.key == pygame.K_q:
                    break
            if event.type == pygame.QUIT:
                break


if __name__ == "__main__":
    main()