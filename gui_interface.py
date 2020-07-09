# -*- coding: utf-8 -*-
from xml_structure import *
from tkinter import *
from gui_structure import element_list, value_elements, value_flux_elements, pop_up
from xml.dom import minidom


def get_flux(var):
    """
    Get the current flux
    :param var:
    :return:
    """
    print(var.get())
    return var.get()


def init_value_flux_elements(flux):
    """
    Initialize the values of all OptionMenu widgets
    :param flux:
    :return:
    """
    for element in element_list[flux]:
        if list(element_list[flux][element])[0] == "OptionMenu":
            value_elements[element] = element_list[flux][element]["OptionMenu"][0]
    value_flux_elements[flux] = value_elements
    print(value_flux_elements)


def save_widgets_values(event, entry, element, flux):
    """
    Saving to a hash table all values of a flux that are entered
    :param event:
    :param entry:
    :param element:
    :param flux:
    :return:
    """
    value_elements[element] = entry.get()
    value_flux_elements[flux] = value_elements
    print(value_flux_elements)


def init_center_widget(frame1, frame2, frame3, flux):
    """
    Creating entry and optionmenu widgets and setting half of them in one frame and the other half in a second frame
    :param frame1:
    :param frame2:
    :param flux:
    :return:
    """
    # Updating the frames and saving all widgets values that are entered
    for element in (element_list[flux]):
        if int((list(element_list[flux].keys())).index(element)) < (abs(-len(element_list[flux]) / 3)):
            frame = frame1
        elif (abs(-len(element_list[flux]) / 3)) <= int((list(element_list[flux].keys())).index(element)) < \
                (abs(-len(element_list[flux]) * 2 / 3)):
            frame = frame2
        else:
            frame = frame3

        if element_list[flux][element] == "Entry":
            label1 = Label(frame, text=element)
            entry1 = Entry(frame, width=20)
            entry1.bind("<KeyRelease>", lambda event,
                                               arg1=entry1,
                                               arg2=element,
                                               arg3=flux: save_widgets_values(event, arg1, arg2, arg3))
            label1.grid(row=int((list(element_list[flux].keys())).index(element)), sticky=E)
            entry1.grid(row=int((list(element_list[flux].keys())).index(element)), column=1)
        elif list(element_list[flux][element].keys())[0] == "OptionMenu":
            label1 = Label(frame, text=element)
            value = StringVar(frame)
            value.set(element_list[flux][element]["OptionMenu"][0])
            optionMenu1 = OptionMenu(frame,
                                     value,
                                     *element_list[flux][element]["OptionMenu"],
                                     command=lambda event,
                                                    arg1=value,
                                                    arg2=element,
                                                    arg3=flux: save_widgets_values(event, arg1, arg2, arg3)
                                     )
            label1.grid(row=int((list(element_list[flux].keys())).index(element)), sticky=E)
            optionMenu1.grid(row=int((list(element_list[flux].keys())).index(element)), column=1, sticky=W)


def update_frame_center(event, frame1, frame2, frame3, variable):
    """
    Updating frames when OptionMenu value change
    :param event:
    :param frame1:
    :param frame2:
    :param variable:
    :return:
    """
    # Get the name of the flux
    flux = get_flux(var=variable)
    # Clear the table that contain all widgets values
    value_elements.clear()
    value_flux_elements.clear()
    # Clear all the center frames
    for widget in frame1.winfo_children():
        widget.destroy()
    for widget in frame2.winfo_children():
        widget.destroy()
    for widget in frame3.winfo_children():
        widget.destroy()
    init_center_widget(frame1=frame1, frame2=frame2, frame3=frame3, flux=flux)
    init_value_flux_elements(flux=flux)


def create_xml():
    """
    Creating xml
    :return:
    """
    try:
        root = minidom.Document()
        selected_template = list(value_flux_elements)[0]
        if selected_template == 'First':
            first_xml(root=root, value_flux_elements=value_flux_elements)
        elif selected_template == 'Second':
            second_xml(root=root, value_flux_elements=value_flux_elements)

        xml_str = root.toprettyxml(indent="", newl="", encoding="utf-8")
        open("test.xml", "w").write(minidom.parseString(xml_str).toprettyxml())
        print("Xml created")
    except:
        pop_up()


class InterfaceGui:
    def __init__(self, window):
        """
        Init the main window
        :param window:
        """
        first_xml_to_show = 'First'
        label = Label(window, text="Choose template")
        flux = StringVar(window)
        flux.set(first_xml_to_show)  # default value
        flux_list = (element_list.keys())
        label.pack()
        # Create frames for the different widgets
        frame_button_bottom = Frame(window, borderwidth=2, relief=GROOVE)
        frame_button_bottom.pack(side=BOTTOM, padx=30, pady=30)
        frame_center = Frame(window, borderwidth=2, relief=GROOVE)
        frame_center.pack(side=BOTTOM, padx=30, pady=30, fill=X)
        frame1 = Frame(frame_center, borderwidth=2, relief=GROOVE)
        frame1.pack(side=LEFT, padx=30, pady=30, fill=X)
        frame2 = Frame(frame_center, borderwidth=2, relief=GROOVE)
        frame2.pack(side=LEFT, padx=30, pady=30, fill=X)
        frame3 = Frame(frame_center, borderwidth=2, relief=GROOVE)
        frame3.pack(side=LEFT, padx=30, pady=30, fill=X)
        menu = OptionMenu(window, flux, *flux_list,
                          command=lambda event,
                                         arg1=frame1,
                                         arg2=frame2,
                                         arg3=frame3,
                                         arg4=flux: update_frame_center(event, arg1, arg2, arg3, arg4))
        menu.pack(side=TOP)
        button = Button(frame_button_bottom,
                        text="Create Xml",
                        command=lambda: create_xml())
        button.pack()
        init_center_widget(frame1=frame1, frame2=frame2, frame3=frame3, flux=first_xml_to_show)
        init_value_flux_elements(flux=first_xml_to_show)
