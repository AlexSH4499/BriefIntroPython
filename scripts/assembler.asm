;hello world
section.text;this is where our base code resides

  global _start; tells kernel where our code starts

_start: ;lets linker know entry point

  mov edx,len ; reg to store message len
  mov ecx,msg ;reg to save message
  mov ebx, 1 ; calls stdout
  mov eax,4 ; sys_write
  int 0x80;calls kernel

  mov eax,1; calss stdout
  int 0x80  ;calls kernel

section .data
msg db 'Hello, World',0xa ; string to print
len equ $ - msg ; length of string
