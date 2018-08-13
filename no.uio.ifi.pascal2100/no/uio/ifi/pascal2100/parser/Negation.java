package no.uio.ifi.pascal2100.parser;

import static no.uio.ifi.pascal2100.scanner.TokenKind.leftParToken;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;

public class Negation extends Factor {

	public Factor fa;

	public Negation(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	public static Negation parse(Scanner s) {
		 
			enterParser("negation");
			Negation neg = new Negation(s.curLineNum());
			s.skip(notToken);
			neg.fa=Factor.parse(s);/*neg.fa.negat= neg;*/
			/*s.readNextToken();*/
			leaveParser("negation");
			return neg;
		}
		
		@Override
		public String identify() {
			// TODO Auto-generated method stub
			return "<negation> " + " on line " + lineNum;
		}
		@Override void prettyPrint() {


			
			Main.log.prettyPrint("not");
			if(fa!=null)fa.prettyPrint();
			
			
			
			}
		@Override
		public void check(Block curScope, Library lib) {
			// TODO Auto-generated method stub
			if (fa != null) fa.check(curScope, lib);
		}
		
	}