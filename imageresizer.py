#! /usr/bin/env python3

import PIL
from PIL import Image
import os
import json
import time


class ImageResizer:
    def imgsizer(self):
        print("[+] Image Resizer Bot Has Started")
        self.filename = []
        with open('/root/imageresizer/fn.json') as f:
            self.stored_fn = json.load(f)
        while True:
            with open('/root/imageresizer/config.json') as f:
                self.configs = json.load(f)
            try:
                for self.dir in self.configs['dirs']:
                    
                    for self.f in os.listdir(self.dir):
                        if self.f.endswith(".jpg") or self.f.endswith(".jpeg ") or self.f.endswith(".png") or self.f.endswith(".gif"):
                            file = [f for f in self.configs['dirs'][self.dir] if not "{}_{}".format(f, self.f) in self.stored_fn]
                            if file:
                                Image.MAX_IMAGE_PIXELS = None
                                try:
                                    self.i = Image.open(self.dir + "/" + self.f)
                                except:
                                    pass
                                # if self.i.size[0] * self.i.size[1] > arbitary_large_limit:
                                #     raise ImageIsToBigError("image size exceeds limit")
                                self.fn, self.fext = os.path.splitext(self.f)
                                try:
                                    # if self.fn.endswith('thumb'):
                                    self.remove = self.configs['dirs'][self.dir]
                                    if self.i.size[0] >= 1600:
                                        self.resize()
                                    elif self.i.size[0] >= 1200:
                                        try:
                                            self.remove.remove(1600)
                                        except:
                                            pass

                                        self.resize()
                                    elif self.i.size[0] >= 802:
                                        try:
                                            self.remove.remove(1600)
                                            self.remove.remove(1200)
                                        except:
                                            pass

                                        self.resize()
                                    elif self.i.size[0] >= 268:
                                        try:
                                            self.remove.remove(1600)
                                            self.remove.remove(1200)
                                            self.remove.remove(802)
                                        except:
                                            pass

                                        self.resize()
                                    elif self.i.size[0] >= 98:
                                        try:
                                            self.remove.remove(1600)
                                            self.remove.remove(1200)
                                            self.remove.remove(802)
                                            self.remove.remove(268)
                                        except:
                                            pass

                                        self.resize()

                                    # elif fn.replace("thumb", ""):
                                    #     filename.append(fn)
                                    #     if fn not in old_fn:
                                    #         if i.size[0] >= 1600:
                                    #             for new_width in configs[dir]:
                                    #                 new_height = int(new_width / i.width * i.height)
                                    #
                                    #                 try:
                                    #                     os.mkdir(dir + "/" + str(new_width))
                                    #                 except:
                                    #                     pass
                                    #
                                    #                 try:
                                    #                     img_folder = '{}/{}'.format(dir, new_width)
                                    #                     if os.path.exists(img_folder):
                                    #                         # PIL.Image.ANTIALIAS
                                    #
                                    #                         i.thumbnail((new_width, new_height))
                                    #                         i.save('{}/{}/{}{}'.format(dir, new_width, fn, fext), optimize=True,
                                    #                                quality=50)
                                    #                         print("Image Resized!")
                                    #                     else:
                                    #                         print("Image Could Not Be Resized")
                                    #                 except:
                                    #                     pass

                                except:
                                    pass
                            else:
                                continue


            except KeyboardInterrupt:
                print("[-] Image Resizer Bot Terminated")

    def resize(self):
        for new_width in self.configs['dirs'][self.dir]:
            if not os.path.exists('{}/{}/{}{}'.format(self.dir, new_width, self.fn, self.fext)) and not "{}_{}".format(new_width, self.f) in self.stored_fn:

                self.new_height = int(new_width / self.i.width * self.i.height)

                try:
                    os.mkdir(self.dir + "/" + str(new_width))
                except:
                    pass

                try:
                    self.img_folder = '{}/{}'.format(self.dir, new_width)
                    if os.path.exists(self.img_folder):
                        self.i.thumbnail((new_width, self.new_height))
                        self.i.save('{}/{}/{}{}'.format(self.dir, new_width, self.fn, self.fext),
                               optimize=True,
                               quality=self.configs['quality'])
                        # self.filename.append("{}_{}".format(new_width, self.f))
                        self.stored_fn.append("{}_{}".format(new_width, self.f))
                        print(self.fn + " Resized into " + str(new_width) + " folder!")
                    else:
                        print(self.fn + " Could not be resized")
                        # return
                except:
                    pass
            elif os.path.exists('{}/{}/{}{}'.format(self.dir, new_width, self.fn, self.fext)) and not "{}_{}".format(new_width, self.f) in self.stored_fn:
                # self.filename.append("{}_{}".format(new_width, self.f))
                self.stored_fn.append("{}_{}".format(new_width, self.f))
                print("[+] " + "{}_{}".format(new_width, self.f) + " Saved")
            else:
                # print(fn + " already exist")
                continue

        with open('/root/imageresizer/fn.json', 'w', encoding='utf-8') as outfile:
            json.dump(self.stored_fn, outfile, ensure_ascii=False, indent=4)

    # def thumb_main_resize(self):
    #     pass


if __name__ == '__main__':
    # imgsizer()
    i = ImageResizer()
    i.imgsizer()
