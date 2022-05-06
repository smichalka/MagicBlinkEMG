import sys
import os
import textwrap
import json
import numpy as np
import random
import string
from markerTests.pylsl import StreamInfo, StreamOutlet
import argparse
import pygame

def lsl_setup(marker_stream_name):
    # LSL
    # first create a new stream info (here we set the name to MyMarkerStream,
    # the content-type to Markers, 1 channel, irregular sampling rate,
    # and string-valued data) The last value would be the locally unique
    # identifier for the stream as far as available, e.g.
    # program-scriptname-subjectnumber (you could also omit it but interrupted
    # connections wouldn't auto-recover). The important part is that the
    # content-type is set to 'Markers', because then other programs will know how
    #  to interpret the content
    info = StreamInfo(marker_stream_name, 'Markers', 1, 0, 'string', 'uidmkrs01')
    # make an outlet
    outlet = StreamOutlet(info)
    outlet.push_sample(['SettingUp'])
    return outlet

def display_sentence(texts,screen,font):
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

def present_stimulus(current_stimulus,screen,font,outlet,marker_codes,trial_num):
    stimulus_text = [" < " + current_stimulus['style'] + " >",current_stimulus['phrase']]
    display_sentence(stimulus_text,screen,font)

    #Send marker to indicate start and output index for silent
    marker_text = marker_codes['begin_speaking'] + str(current_stimulus['phrase_num'])+ marker_codes[current_stimulus['style']] +  str(trial_num)
    outlet.push_sample([marker_text])

def determine_next_stimulus(phrases,trial_num,args):
    num_rounds = int(args.num_rounds)
    num_styles = len(args.exp_style)
    num_phrases = len(phrases)

    # Check to see if this is the last one
    if trial_num < (num_rounds * num_styles * num_phrases)-1:
        last_one = False
    else:
        last_one = True

    # This version just rotates through the options advancing in order
    # say the same phrase in all conditions, then move to the next
    style_num = int(np.mod(trial_num,num_styles)) #flip back and forth between styles
    phrase_num = int(np.mod(((trial_num - style_num) / num_styles),num_phrases)) # account for styles then mod w/ phrases
    next_stimulus = {'phrase':phrases[phrase_num],'phrase_num':phrase_num,'style':args.exp_style[style_num],'style_num':style_num,'trial_num':trial_num,'last_one':last_one}

    return next_stimulus



def initialize_files(args):
    # Create output director
    if os.path.isdir(args.output_dir) == False:
        os.makedirs(args.output_dir, exist_ok=False)
    # Create log file
    # TODO

def initiate_quit(args):
    # Save file

    pygame.quit() 
    return False #running = false
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

def parse_args(args):
    parser = argparse.ArgumentParser('Process Audio Data')

    parser.add_argument(
        '--phrases',
        type=str,
        nargs='*',
        default=['next','back','select','previous']
    )
    parser.add_argument(
        '--output_dir',
        type=str,
        default="./log/"
    )
    parser.add_argument(
        '--logfilename',
        type = str,
        default="test_info.json"
    )
    parser.add_argument(
        '--exp_style',
        type = str,
        nargs='*',
        default = ['normal','quiet']
    )
    parser.add_argument(
        '--num_rounds',
        type = int,
        default = 3
    )
    return parser.parse_args(args)



def main(args):
    args = parse_args(args)
    phrases = args.phrases


    # Make appropraite directories and log files
    initialize_files(args)

    # Setup LSL
    marker_stream_name = 'MarkersForBooks'
    marker_codes = {'quiet':'Q','normal':'N','begin_speaking':'b','end_speaking':'e'}
    outlet = lsl_setup(marker_stream_name)
    # check to make sure all conditions included in marker code
    try:
        for exp in args.exp_style:
            print(marker_codes[exp])
    except:
        print("Missing one of the experiment styles in marker_codes.")

    # initialising pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    font = pygame.font.SysFont(None, 54)

    display_sentence(["Press any key to begin"],screen,font)
    #Wait for a key press to start
    wait_for_keypress()
    
    # Initiate experiment

    # Send marker to indicate start
    display_sentence(["Type 'q' to quit,", "'n' or ' ' for next,", "'c' when completed speaking"],screen,font)
    outlet.push_sample(['Start'])
    pygame.display.update()
    pygame.time.delay(1000)


    running = True
    begin_trial = True
    trial_num = 0
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_n or event.key == pygame.K_SPACE) and begin_trial:
                    #Determine what to display next (phrase, condition)
                    current_stimulus = determine_next_stimulus(phrases,trial_num,args)
                    present_stimulus(current_stimulus,screen,font,outlet,marker_codes,trial_num)

                    pygame.time.delay(100)
                    
                    begin_trial=False
                    
                elif event.key == pygame.K_c or event.key == pygame.K_SPACE:

                    #Send marker to indicate start and output index for silent
                    marker_text = marker_codes['end_speaking'] + str(current_stimulus['phrase_num'])+ marker_codes[current_stimulus['style']] +  str(trial_num)
                    outlet.push_sample([marker_text])
                    display_sentence([' '],screen,font)
                    
                    if current_stimulus['last_one']:
                        running = initiate_quit(args)
                    else:
                        begin_trial = True
                        trial_num +=1


                elif event.key == pygame.K_q:
                    # Save the file
                    running = initiate_quit(args)
            if event.type == pygame.QUIT:
                # Save the file
                running = initiate_quit(args)
                break
                    
if __name__ == "__main__":
    main(sys.argv[1:])