import os

import cv2


class VideoSplit:
    """
        将视频分帧为图片
        source_path: 视频文件存储地址
        result_path： 图片结果文件保存地址
        frame: 帧率，每frame帧保存一张图片
    """

    def __init__(self, source_path, result_path, frame=1):
        self.source_path = source_path
        if not os.path.exists(self.source_path):
            raise Exception("源文件路径不存在！")

        self.result_path = result_path
        self.frame = frame

        if not os.path.exists(self.result_path):
            os.makedirs(self.result_path)
            print("创建文件夹{},".format(self.result_path))

    def split_video(self):
        # 获取视频文件名列表
        video_list = os.listdir(self.source_path)
        for i, name in enumerate(video_list):
            # 获取每个视频文件的路径
            video_list[i] = os.path.join(self.source_path, name)

            # 视频文件的名称
            basename = name.split('.')[0]

            # 以视频文件名称创建子文件夹，分别保存每个视频的图片文件
            video_result_path = os.path.join(self.result_path, basename)
            if not os.path.exists(video_result_path):
                os.makedirs(video_result_path)
                print("创建子文件夹{},".format(basename))

            # 利用VideoCapture捕获视频
            cap = cv2.VideoCapture(video_list[i])
            print("视频{}开始分帧...".format(name))

            # sum用于计算多少帧保存一次图片
            sum = 0
            i = 0  # i表示为图片数量
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                sum += 1
                # 保存图片
                if sum == self.frame:
                    sum = 0
                    i += 1
                    imgname = basename + '_' + str(i) + '.jpg'
                    imgPath = os.path.join(video_result_path, imgname)
                    cv2.imwrite(imgPath, frame)
                    print(imgname)
            print("{}视频文件提取完成".format(basename))

        print("完成")
if __name__ == "__main__":
    source_path = r''
    result_path = r''
    tst = VideoSplit(source_path, result_path)
    tst.split_video()