import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:stacionar_app/constants/colors.dart';
import 'package:stacionar_app/constants/sizes.dart';
import 'package:stacionar_app/features/core/navigation_tabs/applications_list/video_player/video_list.dart';
import 'package:stacionar_app/widgets/contrained_container.dart';
import 'package:video_player/video_player.dart';

class VideoScreen extends StatefulWidget {
  const VideoScreen({Key? key, required this.thumbnail, required this.video, required this.season, required this.title})
      : super(key: key);

  final String title;
  final String season;
  final String thumbnail;
  final String video;

  @override
  State<VideoScreen> createState() => _VideoScreenState();
}

class _VideoScreenState extends State<VideoScreen> {
  late VideoPlayerController _controller;

  @override
  void initState() {
    VideoTypes videoAsset = videoType.firstWhere(
      (type) => type.video == widget.video,
    );
    super.initState();
    _controller = VideoPlayerController.asset(videoAsset.video);

    _controller.addListener(() {
      setState(() {});
    });
    _controller.initialize().then((_) => setState(() {}));
    // _controller.setLooping(true); // Loop the video
    // _controller.play(); // Play the video once finished loading
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    var isDark = Get.isDarkMode;
    var iconColor = isDark ? Colors.white70 : Colors.black54;
    var containerBorderColor = isDark ? jPrimaryDarkContainerColor : jPrimaryLightContainerColor;
    var containerColor = isDark ? jPrimaryDarkColor : jPrimaryLightColor;

    var scaffoldImage = isDark ? 'assets/images/pusheenbg_dark.jpeg' : 'assets/images/pusheenbg_light.jpeg';
    VideoTypes videoAsset = videoType.firstWhere(
      (type) => type.video == widget.video,
    );
    return SafeArea(
      child: Scaffold(
        floatingActionButton: Align(
          alignment: Alignment.topLeft,
          child: Padding(
            padding: const EdgeInsets.all(30.0),
            child: FloatingActionButton(
              foregroundColor: Colors.white,
              backgroundColor: Colors.greenAccent.withOpacity(0.3),
              onPressed: () {
                Navigator.pop(context);
              },
              child: const Icon(Icons.arrow_back),
            ),
          ),
        ),
        body: ConstrainedContainer(
          child: Container(
            decoration: BoxDecoration(image: DecorationImage(fit: BoxFit.cover, image: AssetImage(scaffoldImage))),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Row(
                  children: [
                    const Spacer(
                      flex: 1,
                    ),
                    Expanded(
                      flex: 4,
                      child: Text(
                        videoAsset.title,
                        style: Theme.of(context).textTheme.displayMedium,
                      ),
                    ),
                    const Spacer(
                      flex: 1,
                    ),
                  ],
                ),
                const SizedBox(height: jDefaultSize),
                Container(
                  decoration: BoxDecoration(
                    border: Border.all(
                      color: containerBorderColor,
                      width: 2,
                    ),
                    borderRadius: BorderRadius.circular(20),
                    color: containerColor,
                  ),
                  padding: const EdgeInsets.all(10),
                  child: AspectRatio(
                    aspectRatio: _controller.value.aspectRatio,
                    child: Stack(
                      alignment: Alignment.bottomCenter,
                      children: <Widget>[
                        VideoPlayer(_controller),
                        _ControlsOverlay(controller: _controller),
                        VideoProgressIndicator(_controller, allowScrubbing: true),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

// Controls, progress bar, play button and playback speed
class _ControlsOverlay extends StatelessWidget {
  const _ControlsOverlay({required this.controller});

  static const List<Duration> _exampleCaptionOffsets = <Duration>[
    Duration(seconds: -10),
    Duration(seconds: -3),
    Duration(seconds: -1, milliseconds: -500),
    Duration(milliseconds: -250),
    Duration.zero,
    Duration(milliseconds: 250),
    Duration(seconds: 1, milliseconds: 500),
    Duration(seconds: 3),
    Duration(seconds: 10),
  ];
  static const List<double> _examplePlaybackRates = <double>[
    0.25,
    0.5,
    1.0,
    1.5,
    2.0,
    3.0,
    5.0,
    10.0,
  ];

  final VideoPlayerController controller;

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        AnimatedSwitcher(
          duration: const Duration(milliseconds: 50),
          reverseDuration: const Duration(milliseconds: 200),
          child: controller.value.isPlaying
              ? const SizedBox.shrink()
              : Container(
                  color: Colors.black26,
                  child: const Center(
                    child: Icon(
                      Icons.play_arrow,
                      color: Colors.white,
                      size: 100.0,
                      semanticLabel: 'Play',
                    ),
                  ),
                ),
        ),
        GestureDetector(
          onTap: () {
            controller.value.isPlaying ? controller.pause() : controller.play();
          },
        ),
        Align(
          alignment: Alignment.topLeft,
          child: PopupMenuButton<Duration>(
            initialValue: controller.value.captionOffset,
            tooltip: 'Caption Offset',
            onSelected: (Duration delay) {
              controller.setCaptionOffset(delay);
            },
            itemBuilder: (BuildContext context) {
              return <PopupMenuItem<Duration>>[
                for (final Duration offsetDuration in _exampleCaptionOffsets)
                  PopupMenuItem<Duration>(
                    value: offsetDuration,
                    child: Text('${offsetDuration.inMilliseconds}ms'),
                  )
              ];
            },
            child: Padding(
              padding: const EdgeInsets.symmetric(
                // Using less vertical padding as the text is also longer
                // horizontally, so it feels like it would need more spacing
                // horizontally (matching the aspect ratio of the video).
                vertical: 12,
                horizontal: 16,
              ),
              child: Text('${controller.value.captionOffset.inMilliseconds}ms'),
            ),
          ),
        ),
        Align(
          alignment: Alignment.topRight,
          child: PopupMenuButton<double>(
            initialValue: controller.value.playbackSpeed,
            tooltip: 'Playback speed',
            onSelected: (double speed) {
              controller.setPlaybackSpeed(speed);
            },
            itemBuilder: (BuildContext context) {
              return <PopupMenuItem<double>>[
                for (final double speed in _examplePlaybackRates)
                  PopupMenuItem<double>(
                    value: speed,
                    child: Text('${speed}x'),
                  )
              ];
            },
            child: Padding(
              padding: const EdgeInsets.symmetric(
                // Using less vertical padding as the text is also longer
                // horizontally, so it feels like it would need more spacing
                // horizontally (matching the aspect ratio of the video).
                vertical: 12,
                horizontal: 16,
              ),
              child: Text('${controller.value.playbackSpeed}x'),
            ),
          ),
        ),
      ],
    );
  }
}
