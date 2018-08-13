package no.uio.ifi.pascal2100.parser;


import java.util.ArrayList;
import java.util.List;

import no.uio.ifi.pascal2100.main.Main;
import no.uio.ifi.pascal2100.scanner.Scanner;
import static no.uio.ifi.pascal2100.scanner.TokenKind.*;

/**
 * <h1>ConstDeclPart</h1>
 *
 * <p>Parse a Pascal ConstDeclPart as per project jernbarndiagram</p>
 *
 * <p>Copyright (c) 2015 by Sameer Sawant</p>
 * 
 */
/* const---ConstDecl--*/
public class ConstDeclPart extends PascalSyntax {
	
	// List structure for getting different constant declarations
	public static List <ConstDecl>constdecllist ; 
	public  ConstDecl cd ;
	public ConstDecl firstconstdecl;
	Block b;
	public ArrayList<ConstDecl> constants = new ArrayList<ConstDecl>(); ;
	
	public ConstDeclPart(int n) {
		super(n);
		// TODO Auto-generated constructor stub
	}
	@Override
	public void check(Block curScope, Library lib) {
		// TODO Auto-generated method stub
		ConstDecl localconst= firstconstdecl;
		while (localconst!=null){
			localconst.check(curScope,lib);
		
			localconst=localconst.nextconstdec;
		
		
		}
		
	}
	@Override
	public String identify() {
		// TODO Auto-generated method stub
		return "<const decl part> " + " on line " + lineNum;
	}
	
	 /**
     * Parse a ConstDeclPart.
     * @param Scanner Tokens.
     * @return the ConstDeclPart object of the parse tree.
     */
	public static ConstDeclPart parse(Scanner s) {
		enterParser("const decl part");
		/*System.out.println("entering perserConst decl part");*/
		
		
		ConstDeclPart p = new ConstDeclPart( s.curLineNum());
		
		
		
		constdecllist = new ArrayList<ConstDecl>(); 
		s.skip(constToken);
		p.firstconstdecl=ConstDecl.parse(s);
		p.constants.add(p.firstconstdecl);
		ConstDecl tempcon= p.firstconstdecl;
		while(s.curToken.kind==nameToken){
			tempcon.nextconstdec=tempcon=ConstDecl.parse(s);
			p.constants.add(tempcon);
			
		}
		
		
		leaveParser("const decl part");
		/*System.out.println("left parserConst decl part");*/
		return p;
		}


	@Override
	void prettyPrint() {
		Main.log.prettyPrintLn();
		Main.log.prettyOutdent();
		Main.log.prettyPrint("const ");
		ConstDecl localconst= firstconstdecl;
		while (localconst!=null){
			localconst.prettyPrint();
		
			localconst=localconst.nextconstdec;
		
		
		}
	 Main.log.prettyPrintLn();
	 
		
	}

	

}
