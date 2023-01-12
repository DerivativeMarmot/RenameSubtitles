import os
import shutil

class Rename:

    def newPath(self):
        self.videos_path = input('Input the file path of the videos(please specify "/" symbol at the end): ')
        self.subs_path = input('Input the file path of the subtitles(please specify "/" symbol at the end): ')

    
    def filter(self, subject:str, action:str, example:str, path) -> list :
        # path = input('Input the file path of the {}: '.format(subject))
        keywords_raw = input('\n\
            Only {} containing this keyword need {}\n\
            example: {} (separate by comma if it\'s a list, no space need)\n\
            or press Enter to select all: '.format(subject, action, example))
        selected = []

        print('---')
        if keywords_raw == '':
            selected = sorted(os.listdir(path))
            for filename in selected:
                print(filename)
        else:
            keywords = keywords_raw.split(',')
            for filename in sorted(os.listdir(path)):
                for kw in keywords:
                    if kw in filename:
                        print(filename)
                        selected.append(filename)
        print('---')
        input('Press Enter to confirm selected {}'.format(subject))

        return selected
    
    
    def rename(self):
        selected_videos = self.filter('videos', 'to have subtitles', '.mkv', self.videos_path)
        selected_subs = self.filter('subtitles', 'to be renamed', '.ass', self.subs_path)

        if len(selected_subs) != len(selected_videos):
            while 1:
                go_on = input('\
        the number of video file and sub file is not identical. This may cause problem!\n\
        Confirm to go on? (Y/N): ')
                if go_on == 'Y' or  go_on == 'y':
                    go_on = True
                    break
                elif go_on == 'N' or  go_on == 'n':
                    go_on = False
                    print('End')
                    exit()
                else:
                    continue
        
        modified_subs = []
        for i in range(len(selected_subs)):
            # print(selected_subs[i])
            # print(selected_videos[i])
            modified_sub = selected_videos[i].replace('.mkv', '.ass')
            modified_subs.append(modified_sub)
            os.rename(self.subs_path + selected_subs[i], self.subs_path + modified_sub)
        
        if input('Copy subtitles to video path?(y/n): ') == 'y':
            for modified_sub in modified_subs:
                shutil.copy(self.subs_path + modified_sub, self.videos_path + modified_sub)