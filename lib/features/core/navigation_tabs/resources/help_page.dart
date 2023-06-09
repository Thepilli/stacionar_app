import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:stacionar_app/constants/colors.dart';
import 'package:stacionar_app/constants/sizes.dart';
import 'package:stacionar_app/widgets/disclaimer_text_widget.dart';
import 'package:stacionar_app/widgets/gallery_pop.dart';
import 'package:stacionar_app/widgets/html_reader_widget.dart';

class HelpPage extends StatefulWidget {
  const HelpPage({super.key});

  @override
  State<HelpPage> createState() => _HelpPageState();
}

class _HelpPageState extends State<HelpPage> {
  final String intro =
      'Ahoj, Dobrý den.\nJmenuji se Jiří a touto cestou bych rád pomohl všem, kteří se - stejně tak jako já - potýkají s nemocí zvanou mentální anorexie, nebo chtějí zjistit více o léčbě poruch příjmu potravy. Po zbytek času si budeme tykat, protože přece jenom je to intimnější téma, a navíc jsme v tom společně jako jedna komunita. Nejsi v tom sama, či sám! Ať už chceš využít jeden z nástrojů aplikace, nebo jen získat více informací jak postupovat s léčbou, věř že je to ten správný krok.\nPo začátku léčby jsem si uvědomil, jak malé, přehlížené, ba dokonce zkreslené, je povědomí o poruchách příjmu potravy a lidech jimi trpícími. A také že není jednoduché najít relevantní informace na jednom místě.\nPostupně jak na aplikaci pracuji, budu doplňovat jednotlivé sekce, ať už jsou to nové články, funkcionality, nebo svůj vlasni příběh.';

  @override
  Widget build(BuildContext context) {
    var isDark = Get.isDarkMode;
    var modalColor = isDark ? jPrimaryDarkContainerColor : jPrimaryLightContainerColor;
    return Scaffold(
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () {
          showModalBottomSheet(
            shape: const RoundedRectangleBorder(
              borderRadius: BorderRadius.only(
                topLeft: Radius.circular(30.0),
                topRight: Radius.circular(30.0),
              ),
            ),
            backgroundColor: modalColor,
            context: context,
            builder: (context) {
              return SizedBox(
                height: 330,
                child: Column(
                  children: [
                    DisclaimerText(disclaimer: intro),
                  ],
                ),
              );
            },
          );
        },
        label: const Text('O mně'),
        icon: const Icon(Icons.info),
      ),
      body: ListView(
        children: [
          buildCard(
            'Lůžkové specializované oddělení',
            'assets/icons/help_oddeleni.png',
            'assets/htmls/1_LF_UK_a_VFN_oddeleni.html',
          ),
          buildCard(
            'Denní stacionář',
            'assets/icons/help_stacionar.png',
            'assets/htmls/1_LF_UK_a_VFN_stacionar.html',
          ),
          buildCard(
            'Specializovaná ambulantní péče',
            'assets/icons/help_ambulance.png',
            'assets/htmls/1_LF_UK_a_VFN_ambulance.html',
          ),
          buildCard(
            'E-clinic',
            'assets/icons/help_e_clinic.png',
            'assets/htmls/e_clinic.html',
          ),
          buildCard(
            'Možnosti léčby',
            'assets/icons/help_lecba.png',
            'assets/htmls/help_lecba.html',
          ),
          buildCard(
            'Následky',
            'assets/icons/help_nasledky.png',
            'assets/htmls/nasledky.html',
          ),
          buildAppCard(
            'Aplikace Nepanikař',
            'assets/icons/help_nepanikar.png',
            'assets/htmls/nepanikar.html',
          ),
        ],
      ),
    );
  }

  Widget buildCard(String title, String image, String htmlFilePath) => Padding(
      padding: const EdgeInsets.all(3.0),
      child: Card(
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(jBorderRadius),
        ),
        child: ExpansionTile(
          leading: Image.asset(image, width: 50, height: 50),
          title: Text(title, style: Theme.of(context).textTheme.labelLarge?.apply(fontSizeFactor: 1.2, fontWeightDelta: 2)),
          children: [
            Padding(
              padding: const EdgeInsets.all(15.0),
              child: HtmlReaderWidget(htmlFilePath: htmlFilePath),
            ),
          ],
        ),
      ));

  Widget buildAppCard(String title, String image, String htmlFilePath) => Padding(
        padding: const EdgeInsets.all(3.0),
        child: Card(
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(jBorderRadius),
          ),
          child: ExpansionTile(
            leading: Image.asset(image, width: 50, height: 50),
            title:
                Text(title, style: Theme.of(context).textTheme.labelLarge?.apply(fontSizeFactor: 1.2, fontWeightDelta: 2)),
            children: [
              Padding(
                padding: const EdgeInsets.all(15.0),
                child: Column(
                  children: [
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: HtmlReaderWidget(htmlFilePath: htmlFilePath),
                    ),
                    const SizedBox(
                      height: 150,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          InkwellPop(
                            imgPath: 'assets/images/nepanikar_app.png',
                          ),
                          InkwellPop(
                            imgPath: 'assets/images/nepanikar_qr.png',
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      );
}
