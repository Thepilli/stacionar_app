import 'package:flutter/foundation.dart';

import 'intro_screen_3.dart';
import 'center_next_button.dart';
import 'intro_screen_4.dart';
import 'intro_screen_2.dart';
import 'intro_screen_1.dart';
import 'top_back_skip_view.dart';
import 'intro_screen_5.dart';
import 'package:flutter/material.dart';

class IntroductionAnimationScreen extends StatefulWidget {
  const IntroductionAnimationScreen({Key? key}) : super(key: key);

  @override
  _IntroductionAnimationScreenState createState() => _IntroductionAnimationScreenState();
}

class _IntroductionAnimationScreenState extends State<IntroductionAnimationScreen> with TickerProviderStateMixin {
  AnimationController? _animationController;

  @override
  void initState() {
    _animationController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 8),
    );
    _animationController?.animateTo(0.0);
    super.initState();
  }

  @override
  void dispose() {
    _animationController?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    var screenWidth = MediaQuery.of(context).size.width;
    print(screenWidth);
    var screenHeight = MediaQuery.of(context).size.height;
    print(screenHeight);
    // print(_animationController?.value);

    return Container(
      child: Scaffold(
        body: Container(
          constraints: kIsWeb && screenWidth > 600
              ? const BoxConstraints(maxWidth: 600)
              : (kIsWeb && screenWidth <= 600 ? const BoxConstraints(maxWidth: 600) : const BoxConstraints(maxWidth: 600)),
          child: ClipRect(
            child: Stack(
              children: [
                Intro(
                  animationController: _animationController!,
                ),
                RelaxView(
                  animationController: _animationController!,
                ),
                CareView(
                  animationController: _animationController!,
                ),
                MoodDiaryVew(
                  animationController: _animationController!,
                ),
                WelcomeView(
                  animationController: _animationController!,
                ),
                TopBackSkipView(
                  onBackClick: _onBackClick,
                  onSkipClick: _onSkipClick,
                  animationController: _animationController!,
                ),
                CenterNextButton(
                  animationController: _animationController!,
                  onNextClick: _onNextClick,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  void _onSkipClick() {
    _animationController?.animateTo(
      0.8,
      duration: const Duration(milliseconds: 1200),
    );
  }

  void _onBackClick() {
    if (_animationController!.value >= 0 && _animationController!.value <= 0.2) {
      _animationController?.animateTo(0.0);
    } else if (_animationController!.value > 0.2 && _animationController!.value <= 0.4) {
      _animationController?.animateTo(0.2);
    } else if (_animationController!.value > 0.4 && _animationController!.value <= 0.6) {
      _animationController?.animateTo(0.4);
    } else if (_animationController!.value > 0.6 && _animationController!.value <= 0.8) {
      _animationController?.animateTo(0.6);
    } else if (_animationController!.value > 0.8 && _animationController!.value <= 1.0) {
      _animationController?.animateTo(0.8);
    }
  }

  void _onNextClick() {
    if (_animationController!.value >= 0 && _animationController!.value <= 0.2) {
      _animationController?.animateTo(0.4);
    } else if (_animationController!.value > 0.2 && _animationController!.value <= 0.4) {
      _animationController?.animateTo(0.6);
    } else if (_animationController!.value > 0.4 && _animationController!.value <= 0.6) {
      _animationController?.animateTo(0.8);
    } else if (_animationController!.value > 0.6 && _animationController!.value <= 0.8) {
      _signUpClick();
    }
  }

  void _signUpClick() {
    Navigator.pop(context);
  }
}
