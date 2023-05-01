import 'package:flutter/material.dart';
import 'package:stacionar_app/pages/bmi/bmi_calculator_screen.dart';
import 'package:stacionar_app/pages/food_menu/food_menu_screen.dart';

import '../../dictionary_page.dart';
import '../../help_page.dart';
import '../fortune_wheel/fortune_wheel_page.dart';
import '../meal_plan/meal_plan_screen.dart';
import 'tab_page_builder.dart';

class TabPage extends StatefulWidget {
  const TabPage({super.key});

  @override
  State<TabPage> createState() => _TabPageState();
}

class _TabPageState extends State<TabPage> {
  // my tabs
  List<Widget> myTabs = [
    const TabPageBuilder(
        label: 'Clanky',
        iconPath: 'assets/icons/tab_icon_dictionary.png'), // blog tab
    const TabPageBuilder(
        label: 'BMI', iconPath: 'assets/icons/tab_icon_bmi.png'), // bmi tab
    const TabPageBuilder(
        label: 'Jidelnicek',
        iconPath: 'assets/icons/tab_icon_plan.png'), // plan tab
    const TabPageBuilder(
        label: 'Stacionar',
        iconPath: 'assets/icons/tab_icon_calendar.png'), // calendar tab
    const TabPageBuilder(
        label: 'Ruleta',
        iconPath: 'assets/icons/tab_icon_loterry.png'), // faq tab
    const TabPageBuilder(
        label: 'Odkazy', iconPath: 'assets/icons/tab_icon_help.png'), // faq tab
  ];

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: myTabs.length,
      child: Scaffold(
        body: SafeArea(
          child: Column(
            children: [
              TabBar(
                tabs: myTabs,
                indicator: BoxDecoration(
                  borderRadius: BorderRadius.circular(12),
                  color: Colors.greenAccent,
                ),
              ),
              Expanded(
                child: TabBarView(
                  children: [
                    const DictionaryPage(),
                    const BmiCalculator(),
                    MealTab(),
                    const FoodMenuScreen(),
                    const FortuneWheelPage(),
                    const HelpPage(),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
