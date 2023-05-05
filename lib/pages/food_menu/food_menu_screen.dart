import 'package:flutter/material.dart';
import 'package:flutter_staggered_grid_view/flutter_staggered_grid_view.dart';

class FoodMenuScreen extends StatefulWidget {
  const FoodMenuScreen({super.key});

  @override
  State<FoodMenuScreen> createState() => _FoodMenuScreenState();
}

class _FoodMenuScreenState extends State<FoodMenuScreen> {
  int weekNumber = 0;
  int cycleNumber = 0;
  bool isNextWeek = false;
  @override
  void initState() {
    super.initState();
    DateTime now = DateTime.now();
    weekNumber = getWeekNumber(now);

    cycleNumber = getCycleNumber(weekNumber);
  }

  int getWeekNumber(DateTime date) {
    int dayOfYear = int.parse(
            date.difference(DateTime(date.year, 1, 1)).inDays.toString()) +
        1;
    int weekNumber = ((dayOfYear - date.weekday + 10) ~/ 7);
    if (weekNumber < 1) {
      weekNumber = 52 + weekNumber;
    }
    return weekNumber;
  }

  int getCycleNumber(int weekNumber) {
    return ((weekNumber - 1) % 5) + 1;
  }

  @override
  Widget build(BuildContext context) {
    debugPrint('weekNumber: ${weekNumber.toString()}');

    if (isNextWeek) {
      cycleNumber = getCycleNumber(weekNumber) + 1;
    } else {
      cycleNumber = getCycleNumber(weekNumber);
    }
    return Padding(
      padding: const EdgeInsets.symmetric(
        horizontal: 15.0,
      ),
      child: ListView(
        scrollDirection: Axis.vertical,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Expanded(
                child: Text(
                  'Co je tento týden \ndobrého k obědu?',
                  style: TextStyle(
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              Column(
                children: [
                  const Padding(
                    padding: EdgeInsets.only(top: 8.0),
                    child: Text(
                      'Příští týden',
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.w400,
                      ),
                    ),
                  ),
                  SizedBox(
                    height: 30,
                    child: Switch(
                      value: isNextWeek,
                      onChanged: (value) {
                        setState(() {
                          isNextWeek = value;
                        });
                      },
                    ),
                  ),
                ],
              ),
            ],
          ),
          const SizedBox(
            height: 30,
          ),
          courseLayout(context, cycleNumber),
        ],
      ),
    );
  }
}

Widget courseLayout(BuildContext context, int cycleNumber) {
  List menu = [
    [
      'Pondělí',
      'Brambory, kuřecí stehno',
      const Color(0xffD3DEFA),
      1,
    ],
    [
      'Úterý',
      'Hamburská pečeně, knedlíky',
      const Color(0xffD3DEFA),
      1,
    ],
    [
      'Středa',
      'Bramborová kaše, karbanátek',
      const Color(0xffD3DEFA),
      1,
    ],
    [
      'Čtvrtek',
      'Rýže, kuře na kari',
      const Color(0xffD3DEFA),
      1,
    ],
    [
      'Pátek ',
      'Bramborová kaše, roláda',
      const Color(0xffD3DEFA),
      1,
    ],
    [
      'Pondělí',
      'Koprová omáčka, hovězí, vejce',
      const Color(0xffD3DEFA),
      2,
    ],
    [
      'Úterý',
      'Kroupová kaše, sekaná, okurka',
      const Color(0xffD3DEFA),
      2,
    ],
    [
      'Středa',
      'Těstoviny, kuře po toskánsku',
      const Color(0xffD3DEFA),
      2,
    ],
    [
      'Čtvrtek',
      'Rýže, hovězí plátek, rajčatový salát',
      const Color(0xffD3DEFA),
      2,
    ],
    [
      'Pátek ',
      'Segedinský guláš, knedlíky',
      const Color(0xffD3DEFA),
      2,
    ],
    [
      'Pondělí',
      'Bramborová kaše, kuře, nádivka',
      const Color(0xffD3DEFA),
      3,
    ],
    [
      'Úterý',
      'Těstoviny, kuře na paprice',
      const Color(0xffD3DEFA),
      3,
    ],
    [
      'Středa',
      'Bramborová kaše, holandský řízek, okurkový salát',
      const Color(0xffD3DEFA),
      3,
    ],
    [
      'Čtvrtek',
      'Svíčková omáčka, knedlíky',
      const Color(0xffD3DEFA),
      3,
    ],
    [
      'Pátek ',
      'Rýže, roláda',
      const Color(0xffD3DEFA),
      3,
    ],
    [
      'Pondělí',
      'Bramborová kaše, file, okurkový salát',
      const Color(0xffD3DEFA),
      4,
    ],
    [
      'Úterý',
      'Houbová omáčka, knedlíky',
      const Color(0xffD3DEFA),
      4,
    ],
    [
      'Středa',
      'Zapačené brambory s kuřecím masem',
      const Color(0xffD3DEFA),
      4,
    ],
    [
      'Čtvrtek',
      'Brambory, Ćevapčići ',
      const Color(0xffD3DEFA),
      4,
    ],
    [
      'Pátek ',
      'Bramborové knedlíky, vepřové, špenát',
      const Color(0xffD3DEFA),
      4,
    ],
    [
      'Pondělí',
      'Bramborové knedlíky, kuře, zeli',
      const Color(0xffD3DEFA),
      5,
    ],
    [
      'Úterý',
      'Rajská omáčka, těstoviny',
      const Color(0xffD3DEFA),
      5,
    ],
    [
      'Středa',
      'Bramborová kaše, rizek, kompot',
      const Color(0xffD3DEFA),
      5,
    ],
    [
      'Čtvrtek',
      'Guláš, knedlíky',
      const Color(0xffD3DEFA),
      5,
    ],
    [
      'Pátek ',
      'Lepenice, uzené',
      const Color(0xffD3DEFA),
      5,
    ],
  ];
  final filteredItems = menu.where((item) => item[3] == cycleNumber).toList();
  debugPrint('cycleNumber: ${cycleNumber.toString()}');

  return MasonryGridView.count(
    shrinkWrap: true,
    physics: const NeverScrollableScrollPhysics(),
    crossAxisCount: 1,
    mainAxisSpacing: 10,
    crossAxisSpacing: 23,
    itemCount: menu.where((item) => item[3] == cycleNumber).length,
    itemBuilder: (BuildContext context, int index) {
      return ClipRRect(
        borderRadius: BorderRadius.circular(16),
        child: Container(
          width: double.infinity,
          height: 50,
          color: filteredItems[index][2],
          child: Row(
            mainAxisAlignment: MainAxisAlignment.start,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Container(
                padding: const EdgeInsets.only(left: 20),
                width: 80,
                child: Text(
                  filteredItems[index][0],
                  style: const TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const VerticalDivider(
                color: Colors.black,
                thickness: 1,
                width: 20,
              ),
              // const DottedLine(
              //   direction: Axis.vertical,
              // ),
              Flexible(
                child: SizedBox(
                  child: Text(
                    filteredItems[index][1],
                    style: const TextStyle(
                      fontSize: 15,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      );
    },
  );
}
