import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Welcome to Flutter',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Welcome to To Foodpicker'),
        ),
        body: Center(
          child: Padding(
            padding: const EdgeInsets.all(2.0),
            child: Card(
              child: Column(mainAxisSize: MainAxisSize.min, children: <Widget>[
                const ListTile(
                  leading: Icon(Icons.album),
                  title: Text("Pasta di mama"),
                  subtitle: Text("goeie pasta van die mama"),
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: <Widget>[
                    TextButton(onPressed: () {}, child: const Text('meer info'))
                  ],
                )
              ]),
            ),
          ),
        ),
      ),
    );
  }
}
