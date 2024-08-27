/****************************************************************************
** Meta object code from reading C++ file 'tm_ros_driver_windows.hpp'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.12.8)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "src/tm_ros_driver_windows.hpp"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'tm_ros_driver_windows.hpp' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.12.8. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_RosPage_t {
    QByteArrayData data[8];
    char stringdata0[118];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_RosPage_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_RosPage_t qt_meta_stringdata_RosPage = {
    {
QT_MOC_LITERAL(0, 0, 7), // "RosPage"
QT_MOC_LITERAL(1, 8, 24), // "send_ui_feed_back_status"
QT_MOC_LITERAL(2, 33, 0), // ""
QT_MOC_LITERAL(3, 34, 22), // "tm_msgs::FeedbackState"
QT_MOC_LITERAL(4, 57, 3), // "msg"
QT_MOC_LITERAL(5, 61, 15), // "send_to_ui_list"
QT_MOC_LITERAL(6, 77, 11), // "std::string"
QT_MOC_LITERAL(7, 89, 28) // "change_control_box_io_button"

    },
    "RosPage\0send_ui_feed_back_status\0\0"
    "tm_msgs::FeedbackState\0msg\0send_to_ui_list\0"
    "std::string\0change_control_box_io_button"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_RosPage[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    1,   29,    2, 0x06 /* Public */,
       5,    1,   32,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       7,    0,   35,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void, 0x80000000 | 3,    4,
    QMetaType::Void, 0x80000000 | 6,    2,

 // slots: parameters
    QMetaType::Void,

       0        // eod
};

void RosPage::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<RosPage *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->send_ui_feed_back_status((*reinterpret_cast< tm_msgs::FeedbackState(*)>(_a[1]))); break;
        case 1: _t->send_to_ui_list((*reinterpret_cast< std::string(*)>(_a[1]))); break;
        case 2: _t->change_control_box_io_button(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (RosPage::*)(tm_msgs::FeedbackState );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&RosPage::send_ui_feed_back_status)) {
                *result = 0;
                return;
            }
        }
        {
            using _t = void (RosPage::*)(std::string );
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&RosPage::send_to_ui_list)) {
                *result = 1;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject RosPage::staticMetaObject = { {
    &QThread::staticMetaObject,
    qt_meta_stringdata_RosPage.data,
    qt_meta_data_RosPage,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *RosPage::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *RosPage::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_RosPage.stringdata0))
        return static_cast<void*>(this);
    return QThread::qt_metacast(_clname);
}

int RosPage::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QThread::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 3;
    }
    return _id;
}

// SIGNAL 0
void RosPage::send_ui_feed_back_status(tm_msgs::FeedbackState _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 0, _a);
}

// SIGNAL 1
void RosPage::send_to_ui_list(std::string _t1)
{
    void *_a[] = { nullptr, const_cast<void*>(reinterpret_cast<const void*>(&_t1)) };
    QMetaObject::activate(this, &staticMetaObject, 1, _a);
}
struct qt_meta_stringdata_MainWindow_t {
    QByteArrayData data[11];
    char stringdata0[189];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_MainWindow_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_MainWindow_t qt_meta_stringdata_MainWindow = {
    {
QT_MOC_LITERAL(0, 0, 10), // "MainWindow"
QT_MOC_LITERAL(1, 11, 28), // "change_control_box_io_button"
QT_MOC_LITERAL(2, 40, 0), // ""
QT_MOC_LITERAL(3, 41, 24), // "send_ui_feed_back_status"
QT_MOC_LITERAL(4, 66, 22), // "tm_msgs::FeedbackState"
QT_MOC_LITERAL(5, 89, 3), // "msg"
QT_MOC_LITERAL(6, 93, 15), // "send_to_ui_list"
QT_MOC_LITERAL(7, 109, 11), // "std::string"
QT_MOC_LITERAL(8, 121, 34), // "click_change_control_box_io_b..."
QT_MOC_LITERAL(9, 156, 27), // "click_clear_response_button"
QT_MOC_LITERAL(10, 184, 4) // "quit"

    },
    "MainWindow\0change_control_box_io_button\0"
    "\0send_ui_feed_back_status\0"
    "tm_msgs::FeedbackState\0msg\0send_to_ui_list\0"
    "std::string\0click_change_control_box_io_button\0"
    "click_clear_response_button\0quit"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_MainWindow[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       6,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       1,       // signalCount

 // signals: name, argc, parameters, tag, flags
       1,    0,   44,    2, 0x06 /* Public */,

 // slots: name, argc, parameters, tag, flags
       3,    1,   45,    2, 0x08 /* Private */,
       6,    1,   48,    2, 0x08 /* Private */,
       8,    0,   51,    2, 0x08 /* Private */,
       9,    0,   52,    2, 0x08 /* Private */,
      10,    0,   53,    2, 0x08 /* Private */,

 // signals: parameters
    QMetaType::Void,

 // slots: parameters
    QMetaType::Void, 0x80000000 | 4,    5,
    QMetaType::Void, 0x80000000 | 7,    2,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void MainWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<MainWindow *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->change_control_box_io_button(); break;
        case 1: _t->send_ui_feed_back_status((*reinterpret_cast< tm_msgs::FeedbackState(*)>(_a[1]))); break;
        case 2: _t->send_to_ui_list((*reinterpret_cast< std::string(*)>(_a[1]))); break;
        case 3: _t->click_change_control_box_io_button(); break;
        case 4: _t->click_clear_response_button(); break;
        case 5: _t->quit(); break;
        default: ;
        }
    } else if (_c == QMetaObject::IndexOfMethod) {
        int *result = reinterpret_cast<int *>(_a[0]);
        {
            using _t = void (MainWindow::*)();
            if (*reinterpret_cast<_t *>(_a[1]) == static_cast<_t>(&MainWindow::change_control_box_io_button)) {
                *result = 0;
                return;
            }
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject MainWindow::staticMetaObject = { {
    &QDialog::staticMetaObject,
    qt_meta_stringdata_MainWindow.data,
    qt_meta_data_MainWindow,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *MainWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *MainWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_MainWindow.stringdata0))
        return static_cast<void*>(this);
    return QDialog::qt_metacast(_clname);
}

int MainWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDialog::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 6)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 6;
    }
    return _id;
}

// SIGNAL 0
void MainWindow::change_control_box_io_button()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
