import time
import matplotlib.pyplot as plt


def plot_main(frames):
    facedet = []
    facerec = []
    head = []
    mouth = []
    spoof = []
    cheat = []
    for frame in frames:
        facedet.append(frame.facedet)
        facerec.append(frame.facerec)
        head.append(frame.head)
        mouth.append(frame.mouth)
        spoof.append(frame.spoof)
        cheat.append(frame.cheat)

    plt.figure(figsize=(12, 20))
    plt.subplot(6, 1, 1)
    plt.plot(facedet, color='red')
    plt.xlabel('frames')
    plt.ylabel('cheat status')
    plt.title("Face Detection")

    plt.subplot(6, 1, 2)
    plt.plot(facerec, color='red')
    plt.xlabel('frames')
    plt.ylabel('cheat status')
    plt.title("Face Recognition")

    plt.subplot(6, 1, 3)
    plt.plot(head, color='red')
    plt.xlabel('frames')
    plt.ylabel('cheat status')
    plt.title("Head-pose Estimation")

    plt.subplot(6, 1, 4)
    plt.plot(mouth, color='red')
    plt.xlabel('frames')
    plt.ylabel('cheat status')
    plt.title("Mouth Open Detection")

    plt.subplot(6, 1, 5)
    plt.plot(spoof, color='red')
    plt.xlabel('frames')
    plt.ylabel('cheat status')
    plt.title("Spoof Detection")

    plt.subplot(6, 1, 6)
    plt.plot(cheat, color='red')
    plt.xlabel('frames')
    plt.ylabel('cheat status')
    plt.title("Estimated cheat probability")
    plt.subplots_adjust(hspace=4.0)
    plt.savefig("proctoring_report/cheat_frames_" + time.strftime("%Y%m%d-%H%M%S") + ".png", dpi=300)
    plt.show()


def cheat_count(segments):
    cheat_count = 0
    for segment in segments:
        if (segment.cheat):
            cheat_count += 1
    return cheat_count


def plot_segments(segments):
    x = []
    y = []
    n = cheat_count(segments)
    for segment in segments:
        x.append(segment.count)
        y.append(segment.cheat)

    # fps_assumed = 5
    segment_time = 10
    plt.figure(figsize=(12, 4))
    plt.plot(x, y, 'r')
    plt.xlabel('Time Segments')
    plt.ylabel('Cheating Suspect Count')
    stats = "Total Time : " + str(len(segments) * segment_time) + " seconds\n" + "Cheating Suspected for : " + str(
        n * segment_time) + " seconds"
    plt.figtext(0.5, 0.9, stats, ha="center", fontsize=12, bbox={"facecolor": "orange", "alpha": 0.5, "pad": 3})
    plt.savefig("proctoring_report/cheating_detection_" + time.strftime("%Y%m%d-%H%M%S") + ".png", dpi=300)
    plt.show()
