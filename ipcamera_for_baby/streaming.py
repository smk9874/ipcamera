from vidgear.gears import PiGear

run_flag = True
frame = None

def start_streaming():

        try:
            stream = PiGear(resolution=(self.width, self.height),
                            framerate=self.fps,
                            logging=True,
                            **self.gearOptions).start()
            return True, stream

        except Exception as e:
            log.error('Can\'t start streaming.' + str(e))
                                             
            return False, None

def streaming_process(gearOptions):

    global run_flag
    global frame

    ret, stream = start_streaming()

    while run_flag:

        frame = stream.read()

    stream.stop()

def get_frame():

    global frame

    return frame

streaming_process()
