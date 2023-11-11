import cv2 
import os 
  
class VideoConverter:
    """Converts video to grayscale images set"""

    @staticmethod
    def ConvertVideo(video_filepath: str, makeGrayScale: bool, scaleFactor: float) -> bool:

        video = cv2.VideoCapture(video_filepath)

        video_name = os.path.basename(video_filepath)
        try:
            if not os.path.exists(f"images/{video_name}"):
                os.makedirs(f'images/{video_name}')
        
        except OSError:
            print("Cant create directory \"images\"")

        current_frame = 0

        print("Staring converting")
        while(True): 
            ret,frame = video.read() 

            if ret: 

                image_name = f'./images/{video_name}/frame' + str(current_frame) + '.jpg'

                if(makeGrayScale):
                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
                    frame = gray_frame

                frame_heigh, frame_width = frame.shape
                down_points = (frame_width // scaleFactor, frame_heigh // scaleFactor)
                resized_down = cv2.resize(frame, down_points, interpolation = cv2.INTER_LINEAR)

                cv2.imwrite(image_name, resized_down) 
        

                current_frame += 1
            else: 
                break
        print(f"Converting {video_name} is complete")
        video.release() 
        cv2.destroyAllWindows() 
