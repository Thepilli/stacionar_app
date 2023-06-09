import 'package:flutter/widgets.dart';
import 'package:stacionar_app/features/core/navigation_tabs/applications_list/fortune_wheel/widgets/fortune_wheel_model.dart';

class FortuneWheelController<T> extends ChangeNotifier {
  FortuneWheelModel<T>? value;

  bool isAnimating = false;
  bool shouldStartAnimation = false;
  bool isFinishedAnimating = false;

  void rotateTheWheel() {
    shouldStartAnimation = true;
    notifyListeners();
  }

  void animationStarted() {
    shouldStartAnimation = false;
    isAnimating = true;
  }

  void setValue(FortuneWheelModel<T> fortuneWheelChild) {
    value = fortuneWheelChild;
    isFinishedAnimating = true;
    notifyListeners();
  }

  void animationFinished() {
    isAnimating = false;
    isFinishedAnimating = true;
    shouldStartAnimation = false;
    notifyListeners();
  }
}
