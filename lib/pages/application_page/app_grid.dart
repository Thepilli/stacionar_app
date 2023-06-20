import 'package:flutter/material.dart';

import '../meal_carousel/meal_carousel.dart';
import '../bmi/bmi_calculator_screen.dart';
import '../food_menu/food_menu_screen.dart';
import '../fortune_wheel/fortune_wheel_page.dart';
import '../relaxation_page/relaxation_list.dart';
import '../video_player/video_list.dart';

class ApplicationGrid extends StatefulWidget {
  const ApplicationGrid({Key? key}) : super(key: key);

  @override
  State<ApplicationGrid> createState() => _ApplicationGridState();
}

class _ApplicationGridState extends State<ApplicationGrid> {
  String features = 'Tady najdeš aplikace které ti pomohou nebo tě alespoň pobaví při každodenních aktivitách';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          child: Column(
            children: [
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  features,
                  textAlign: TextAlign.center,
                  style: Theme.of(context).textTheme.headlineLarge,
                ),
              ),
              GridView.count(
                physics: const NeverScrollableScrollPhysics(),
                primary: true,
                crossAxisCount: 1,
                crossAxisSpacing: 0,
                scrollDirection: Axis.vertical,
                mainAxisSpacing: 10,
                shrinkWrap: true,
                childAspectRatio: 3,
                padding: const EdgeInsets.only(left: 24, right: 24),
                children: [
                  itemTile(
                    context,
                    'assets/icons/tab_icon_bmi.png',
                    'Kalkulačka BMI',
                    'Výpočet BMI je velmi snadný, postačí ti k němu tovje váha a výška',
                    'BmiCalculator',
                  ),
                  itemTile(
                    context,
                    'assets/icons/tab_icon_calendar.png',
                    'Týdenní jídelníček',
                    'Zajímá tě jaký jídelníček máme na tento týden?',
                    'FoodMenuScreen',
                  ),
                  itemTile(
                    context,
                    'assets/icons/tab_icon_loterry.png',
                    'Pečivová ruleta',
                    'Nebaví tě lámat si hlavu tím, jaké pečivo se dnes dáš?',
                    'FortuneWheelPage',
                  ),
                  itemTile(
                    context,
                    'assets/icons/tab_icon_gallery.png',
                    'Jídelní inspirace',
                    'Nebo jen hledáš inspiraci co si naplánovat? Zkus se podívat do galerie',
                    'VerticalSliderDemo',
                  ),
                  itemTile(
                    context,
                    'assets/icons/tab_icon_relaxation.png',
                    'Relaxační nahrávky',
                    'Potřebuješ se uklidnit? Zkus si pustit některou z našich relaxačních nahrávek',
                    'RelaxationList',
                  ),
                  itemTile(
                    context,
                    'assets/icons/tab_icon_pusheen.png',
                    'Příběhy Pušínka',
                    'Máš chvilu a potřebuješ se odreagovat? Zkus si pustit některý z příběhů Pušínka',
                    'VideoList',
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

Widget itemTile(BuildContext context, String iconPath, String title, String description, String pageName) {
  return ListTile(
    onTap: () {
      String nextPage = pageName; // Replace 'ArticleNavigationPage' with the desired page name

      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => getPageByName(nextPage),
        ),
      );
    },
    leading: Image.asset(
      iconPath,
    ),
    title: Padding(
      padding: const EdgeInsets.only(top: 8.0, bottom: 8.0),
      child: Text(
        title,
        style: Theme.of(context).textTheme.labelLarge?.apply(fontSizeFactor: 1.2, fontWeightDelta: 2),
      ),
    ),
    subtitle: Column(
      children: [
        Text(
          description,
          style: Theme.of(context).textTheme.labelLarge?.apply(
                fontSizeFactor: 0.9,
              ),
        ),
      ],
    ),
  );
}

Widget getPageByName(String pageName) {
  // Add your logic to return the appropriate widget based on the page name
  // For example:
  if (pageName == 'BmiCalculator') {
    return const BmiCalculator();
  }
  if (pageName == 'FoodMenuScreen') {
    return const FoodMenuScreen();
  }
  if (pageName == 'FortuneWheelPage') {
    return const FortuneWheelPage();
  }
  if (pageName == 'RelaxationList') {
    return const RelaxationList();
  }
  if (pageName == 'VideoList') {
    return const VideoList();
  }
  if (pageName == 'VerticalSliderDemo') {
    return const MealCarousel(
      meals: [],
    );
  }
  // Add more conditions for other page names if needed
  return Container(); // Default return value if no matching page name is found
}
