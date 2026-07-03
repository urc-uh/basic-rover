# Getting Started with ROS

## Installation

Read through and follow the steps the [Installation](https://docs.ros.org/en/lyrical/Installation.html) section of the ROS 2 Documentation or, if you prefer installing ROS inside a container, follow [Installing in a Container](#installing-in-a-container) on this page.
ROS is very tied to the OS, so isolating the system all its packages are installed on with a container may make your life easier.

> [!IMPORTANT]
> It is _highly_ recommended that you use binary packages with one of the Tier 1 supported platforms: Ubuntu 26.04, RHEL-10, or Windows 11.
> If you are using macOS or another unsupported OS, consider dual booting or using a container before building from source or using an unsupported package manager unless you are sure you know what you are doing.

> [!NOTE]
> The current Software Team lead does not have experience with ROS on Windows and is unfamiliar with the Windows terminal, so you may have a harder time getting help if you use Windows.
> You can try using [WSL](https://learn.microsoft.com/windows/wsl) by following the setup instructions [here](https://github.com/espanakk/ros2-wsl2-guide) to install ROS in a Ubuntu terminal environment in Windows (and integrate with VSCode), but you may come across issues at some point.


### Installing in a Container

> [!TIP]
> This section was adapted from [this tutorial](https://iris-its.github.io/setup-ros-distrobox).
> It contains an additional section on integrating Visual Studio Code (VSCode).
> VSCode is a great IDE to work in at any level, and the integrated terminal will come in handy working with ROS.
> Alternatively, the ROS documentation contains a guide to [set up ROS 2 with VSCode and Docker](https://docs.ros.org/en/lyrical/How-To-Guides/Setup-ROS-2-with-VSCode-and-Docker-Container.html).

If you do not have a compatible OS or prefer a separate environment, you can install ROS inside a container.
I recommend using [`distrobox`](https://distrobox.it) with [`podman` without root privileges](https://distrobox.it/compatibility/#install-podman-in-a-static-manner) as the container manager.
After installing `distrobox` and a container manager, create a Ubuntu container with ROS Lyrical Luth pre-installed like so:
```console
user@host:~$ distrobox create --image docker.io/osrf/ros:lyrical-desktop --name urc --hostname urc --additional-packages "unminimize"
```
The name can be whatever you want, setting a hostname is optional, and any other packages you want initially installed can be added after `unminimize`, separating all packages with spaces (e.g. `--additional-packages "unminimize neovim zoxide"`).
By default the distrobox container will share your user's home, but if you want to avoid cluttering your home directory with `.ros`, `.colcon`, `.rviz2`, etc. you can specify a different home directory with `--home /container/home/directory`.
For more options and information see the [`distrobox-create` documentation](https://distrobox.it/usage/distrobox-create).

Next, enter your container:
```console
user@host:~$ distrobox enter urc  # or whatever name you used, this may take a few minutes
user@urc:~$ sudo unminimize  # this will add packages and files missing from ubuntu-minimal, recommended but not required
user@urc:~$ sudo apt update && sudo apt upgrade  # updates your system and all your packages
```
Then complete any other setup you would like.
If you didn't set a separate home directory during the create command, your home directory shouldn't change and your dotfiles should work out of the box if you are using a different Linux distribution.

You now have a full ROS 2 installation and do not need to follow any instructions in the Installation section of the ROS Documentation.


## ROS Primer

[ROS](https://docs.ros.org/en/lyrical/About-ROS.html) (Robot Operating System) is a framework and collection of tools and libraries we will use to program the rover.
It facilitates using mature libraries to solve many of the more difficult robotics programming challenges, interacting with and observing a robot from a different computer, and using several programs that are useful for debugging, testing, and data visualization purposes.
The way ROS runs also allows us to write modular code, meaning if we write our packages correctly we should be able to reuse the code with an entirely different robot (or just an updated version of our rover) with little adjustment.

A good way to familiarize yourself with the basics of working in ROS is to work through the [beginner](https://docs.ros.org/en/lyrical/Tutorials/Beginner-CLI-Tools.html) [tutorials](https://docs.ros.org/en/lyrical/Tutorials/Beginner-Client-Libraries.html).
Make sure you actually follow the instructions, don't just read them, especially if working in a terminal environment is new to you.
They can be a little tedious, but getting comfortable in the environment and familiar with how the ROS-specific code looks will help _a lot_ starting out.

When working through [Creating a workspace](https://docs.ros.org/en/lyrical/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html) make a new empty workspace, and use it for the rest of the tutorials.
This will help avoid accidentally cluttering this workspace with unrelated code.
Do come back to this workspace and try to find or test things you are learning in this codebase, and experiment with the examples you create in the tutorials.

When you get to the programming-based tutorials, follow the Python tutorials as we will write most of our code in Python.
If you are comfortable in C++ you can also work through those tutorials if you would like.
However, note we will only use C++ if we need to use a C++ library specifically, and possibly to rewrite certain programs if speed becomes an issue, though this is unlikely.


### Interfaces

Some of the most important things to understand conceptually are [interfaces](https://docs.ros.org/en/lyrical/Concepts/Basic/Interfaces-Topics-Services-Actions.html) as these are how we will communicate between different systems on the rover.
For example, most sensors will have an associated publisher constantly updating a [topic](https://docs.ros.org/en/lyrical/Concepts/Basic/About-Topics.html), stateful data or data processing may be handled through a [service](https://docs.ros.org/en/lyrical/Concepts/Basic/About-Services.html), and anything involving motion will be initiated through an [action](https://docs.ros.org/en/lyrical/Concepts/Basic/About-Actions.html).
Reference back to these articles anytime interfaces come up while you work through the tutorials and as you begin working in ROS.
See if you can understand why the particular interface (topic, service, or action) was selected for the application and when a different interface might be appropriate.
