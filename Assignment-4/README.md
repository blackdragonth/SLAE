  This encoder will XOR pseudo-randomly generated "VALUE" to individual byte of shellcode, this "VALUE" can be considered a KEY. 
After that, this KEY, again, will be added(+) to each byte of shellcode. Finally the order of the encoded shellcode will be reversed.
  
  The KEY will be pseudo-randomly generated (0x01 - 0xff), a weak one, absolutely, to reduce the time used for decoding.
  
  * For this technique to be effective, a maker value "0xD3"+KEY will be appended to the encoded shellcode. Surely, this can be changed.

  * To avoid overflow possibility, the byte value 0xf1-0xff will be skipped at the addition stage.

--------------------------------------------------------------------------------------------------------------------

The docoder stub will try to bruteforce the KEY at runtime, subtract the KEY from each byte of the shellcode, xor it back, reverse the shellcode to its original order, and then execute the shellcode.

The decode stub should be adjust accordingly. 
