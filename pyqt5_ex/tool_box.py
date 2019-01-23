def init_UI(self):
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle('Dragonfly Classifier')
        self.setGeometry(0,0,1100,900)
        window = QtWidgets.QWidget()
        hbox = QtWidgets.QHBoxLayout()
        hbox.setSpacing(0)

        self.frame_panel = frame_panel.Frame_panel(self)
        hbox.addWidget(self.frame_panel)

        window.setLayout(hbox)
        self.setCentralWidget(window)
        self.show()

        self.manual_panel = manual.Manual_panel(self)
        self.conversion_panel = conversion.Conversion_panel(self)
        self.embedding_panel = embedding.Embedding_panel(self)
        self.mlp_panel = mlp.MLP_panel(self)

        # Menu items
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        # Theme picker
        thememenu = menubar.addMenu('&Theme')
        self.theme = QtWidgets.QActionGroup(self, exclusive=True)
        for i, s in enumerate(map(str, list(QtWidgets.QStyleFactory.keys()))):
            a = self.theme.addAction(QtWidgets.QAction(s, self, checkable=True))
            if i == 0:
                a.setChecked(True)
            a.triggered.connect(self.theme_changed)
            thememenu.addAction(a)
        # Color map picker
        cmapmenu = menubar.addMenu('&Color Map')
        self.color_map = QtWidgets.QActionGroup(self, exclusive=True)
        for i, s in enumerate(['cubehelix', 'CMRmap', 'gray', 'gray_r', 'jet']):
            a = self.color_map.addAction(QtWidgets.QAction(s, self, checkable=True))
            if i == 0:
                a.setChecked(True)
            a.triggered.connect(self.cmap_changed)
            cmapmenu.addAction(a)

        toolbox = QtWidgets.QToolBox(self)
        hbox.addWidget(toolbox)
        toolbox.setFixedWidth(300)
        toolbox.addItem(QtWidgets.QWidget(self), '&Display')
        toolbox.addItem(self.manual_panel, '&Manual')
        toolbox.addItem(self.conversion_panel, '&Conversion')
        toolbox.addItem(self.embedding_panel, '&Embedding')
        toolbox.addItem(self.mlp_panel, 'M&LP')
        toolbox.currentChanged.connect(self.tab_changed)