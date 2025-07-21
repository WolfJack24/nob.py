# nob.py

The great Header-only build tool [[nob.h](https://github.com/Tsoding/nob.h)] in Python

> Please understand if this never materialise, i don't really know if i will be able to achieve everything that C cn do in Python.
> It would actullay make more sense to write a nob.cs, since C# allows - and i quote - 'unsafe' code with

```cs
unsafe {  }
```

> blocks.
> Maybe i should do that, cuase nob.h proves poiters are necessary.
> If someone wants to attempt this, they can, i haven't bought the idea so it's free for anyone, so i might archive this repo, and make nob.cs.
> I will upload what i have - which isn't much, but you can build of it.
> so Good Luck!

## TODO

- Well... Implement the whole thing in Python ofc! Meaning it's not a wrapper for a .dll, .lib, .so, or anything.
- This means everthing including Dynamic Arrays.
- it must compile on ALL operating systems (Windows, Linux and OSX).
- Figure out how to interface to libc to access malloc, realloc and so on.

This project will focus on the Windows build then it will continue onto Linux and OSX will just have work, cause i don't have a MacBook... maybe people will comfirm it works, idk.

### Platforms

Windows:

- Version 24H2 (OS Build 26100.4652)

Linux:

- WSL installed with Debian (TODO!)

OSX:

- Whatever is the latest (can't keep track)

### Compilers

Python:

- 3.13.5
