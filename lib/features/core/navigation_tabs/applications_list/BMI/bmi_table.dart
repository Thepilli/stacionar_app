import "package:flutter/material.dart";

class BmiTable extends StatelessWidget {
  const BmiTable({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(15.0),
          child: Table(
            border: TableBorder.all(),
            defaultVerticalAlignment: TableCellVerticalAlignment.middle,
            children: [
              const TableRow(
                decoration: BoxDecoration(),
                children: [
                  TableCell(
                    verticalAlignment: TableCellVerticalAlignment.middle,
                    child: Padding(
                      padding: EdgeInsets.all(8.0),
                      child: Text(
                        "BMI",
                        style: TextStyle(decoration: TextDecoration.none, fontSize: 20),
                      ),
                    ),
                  ),
                  TableCell(
                    verticalAlignment: TableCellVerticalAlignment.middle,
                    child: Padding(
                      padding: EdgeInsets.all(8.0),
                      child: Text(
                        "Hodnota Indexu",
                        style: TextStyle(decoration: TextDecoration.none, fontSize: 20),
                      ),
                    ),
                  ),
                ],
              ),
              buildCustomTableRow("< 18,5", "Podváha"),
              buildCustomTableRow("18,5–24,9", "Optimální váha"),
              buildCustomTableRow("25,0–29,9", "Nadváha"),
              buildCustomTableRow("30,0 ≤	", "Obezita"),
            ],
          ),
        ),
      ),
    );
  }
}

TableRow buildCustomTableRow(String bmiString, String indexString) {
  return TableRow(
    decoration: const BoxDecoration(),
    children: [
      TableCell(
        verticalAlignment: TableCellVerticalAlignment.middle,
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Text(
            bmiString,
            style: const TextStyle(decoration: TextDecoration.none, fontSize: 20),
          ),
        ),
      ),
      TableCell(
        verticalAlignment: TableCellVerticalAlignment.middle,
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Text(
            indexString,
            style: const TextStyle(decoration: TextDecoration.none, fontSize: 20),
          ),
        ),
      ),
    ],
  );
}
